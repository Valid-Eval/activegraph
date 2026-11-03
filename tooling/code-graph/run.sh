#!/bin/bash
# Build a Graphify code graph of one git repository with the network denied.
#
#   tooling/code-graph/run.sh <repo-path> [<subdir, default lib>] [<name>]
#
# Works on a clone under $CODE_GRAPH_WORK (default ~/code-graph-work), so the
# target repository is never written to and untracked files never get read.
# macOS only: the no-network guarantee is sandbox-exec. Needs Python 3.12,
# which the dependency lock was resolved for.
#
# The only network use is pip installing the hash-locked wheels, before any
# code is read. The script stops if its own controls fail, or if the audit
# hook logs a socket event during extraction.
set -euo pipefail

die() { echo "code-graph: $*" >&2; exit 1; }

[[ $# -ge 1 ]] || die "usage: run.sh <repo-path> [<subdir>] [<name>]"
[[ "$(uname)" == "Darwin" ]] || die "needs macOS sandbox-exec; no other no-network control is implemented"

HERE="$(cd "$(dirname "$0")" && pwd -P)"
TARGET="$(cd "$1" && pwd -P)"
SUBDIR="${2:-lib}"
NAME="${3:-$(basename "$TARGET")}"
[[ "$NAME" =~ ^[A-Za-z0-9_][A-Za-z0-9._-]*$ ]] || die "name must be letters, digits, dot, dash or underscore: $NAME"
[[ "$(git -C "$TARGET" rev-parse --show-toplevel 2>/dev/null)" == "$TARGET" ]] || die "$TARGET is not a git repository root"
[[ -d "$TARGET/$SUBDIR" ]] || die "no $SUBDIR in $TARGET"

mkdir -p "${CODE_GRAPH_WORK:-$HOME/code-graph-work}"
WORK="$(cd "${CODE_GRAPH_WORK:-$HOME/code-graph-work}" && pwd -P)"
case "$WORK" in
  "$TARGET"|"$TARGET"/*) die "CODE_GRAPH_WORK must be outside the target repository" ;;
esac
case "$TARGET" in
  "$WORK"/*) die "the target must be outside CODE_GRAPH_WORK, which this script clears" ;;
esac
mkdir -p "$WORK/home" "$WORK/tmp" "$WORK/src" "$WORK/out" "$WORK/logs"

PY="${PYTHON:-python3.12}"
[[ "$("$PY" -c 'import sys; print("%d.%d" % sys.version_info[:2])')" == "3.12" ]] || die "$PY is not Python 3.12"

if [[ ! -x "$WORK/venv/bin/graphify" ]]; then
  "$PY" -m venv "$WORK/venv"
  "$WORK/venv/bin/pip" -q install --only-binary :all: --require-hashes --no-deps \
    -r "$HERE/requirements-graphify-0.9.97.lock"
fi

SB="$WORK/nonet.sb"
cat > "$SB" <<EOF
(version 1)
(allow default)
(deny network*)
(deny file-write*)
(allow file-write* (subpath "$WORK") (subpath "/private/var/folders") (literal "/dev/null") (literal "/dev/dtracehelper") (literal "/dev/tty"))
EOF

jail() {
  env -i HOME="$WORK/home" PATH=/usr/bin:/bin TMPDIR="$WORK/tmp" GRAPHIFY_BACKEND=none \
    PYTHONPATH="$HERE/audit" CODE_GRAPH_AUDIT="$AUDIT" \
    sandbox-exec -f "$SB" "$@"
}

# Controls: a control only counts once it has been seen to refuse something.
AUDIT="$WORK/logs/control.jsonl"
: > "$AUDIT"
CONNECT='import socket; socket.create_connection(("1.1.1.1", 443), 3).close()'
if jail "$WORK/venv/bin/python" -c "$CONNECT" 2>/dev/null; then
  die "control failed: a socket connected inside the sandbox"
fi
grep -q 'socket.connect' "$AUDIT" || die "control failed: the audit hook did not log a known socket call"
PROBE="$HOME/.code-graph-write-probe.$$"
if jail /bin/sh -c "echo x > '$PROBE'" 2>/dev/null; then
  rm -f "$PROBE"
  die "control failed: a write outside $WORK succeeded inside the sandbox"
fi
if ! "$WORK/venv/bin/python" -c "$CONNECT" 2>/dev/null; then
  echo "code-graph: note: no network outside the sandbox either, so the block above proves less" >&2
fi

CLONE="$WORK/src/$NAME"
rm -rf "$CLONE" "${WORK:?}/out/$NAME"
git clone -q --no-hardlinks "$TARGET" "$CLONE"
mkdir -p "$WORK/out/$NAME"

AUDIT="$WORK/logs/$NAME.jsonl"
: > "$AUDIT"
(cd "$CLONE" && jail "$WORK/venv/bin/graphify" extract "$SUBDIR" --code-only) > "$WORK/logs/$NAME.extract.log" 2>&1 \
  || die "extract failed; see $WORK/logs/$NAME.extract.log"
for d in "$CLONE/$SUBDIR/graphify-out" "$CLONE/graphify-out"; do
  if [[ -d "$d" ]]; then mv "$d" "$WORK/out/$NAME/graphify-out"; break; fi
done
[[ -s "$WORK/out/$NAME/graphify-out/graph.json" ]] || die "no graph.json; see $WORK/logs/$NAME.extract.log"
(cd "$WORK/out/$NAME" && jail "$WORK/venv/bin/graphify" cluster-only . --no-label --no-viz) > "$WORK/logs/$NAME.report.log" 2>&1 \
  || die "report failed; see $WORK/logs/$NAME.report.log"

if grep -qE '"(socket|urllib|http\.client)\.' "$AUDIT"; then
  die "network use attempted during the run; see $AUDIT"
fi

GRAPH="$WORK/out/$NAME/graphify-out/graph.json"
echo "commit: $(git -C "$CLONE" rev-parse HEAD)"
echo "graph:  $GRAPH"
echo "report: $WORK/out/$NAME/graphify-out/GRAPH_REPORT.md"
echo "source: $CLONE/$SUBDIR"
echo "audit:  0 socket events ($AUDIT)"
