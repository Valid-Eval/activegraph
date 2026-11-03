# Code-graph map and harness

A static map of this gem and neo4j-ruby-driver, with the work already done so nobody needs to repeat it. Not loaded by the gem: `activegraph.gemspec` packages only `bin`, `lib` and `config`.

## Start here, to avoid recomputing

| Instead of | Use | Saves |
|---|---|---|
| Installing and vetting a tool, running it | `results/<repo>/graph.json.gz` and `GRAPH_REPORT.md` | Install, extraction, the egress check |
| Reading code to find seams and hubs | "Answers you can reuse" in `FINDINGS.md`, with file:line | Most of the reading tokens |
| Hand-checking whether edges can be trusted | Sample tables and read rules in `FINDINGS.md` | The sampling |
| Evaluating CodeGraph on Ruby | The verdict in `FINDINGS.md` | A full evaluation |
| Re-checking a tool upgrade by eye | `known_edges.py` and `known-edges/*.json` | Re-verification; it fails loudly |
| Asking "does it handle `has_many`?" | The fixture table in `FINDINGS.md` | Writing a test tree |

Query a stored graph without installing anything:

```bash
gunzip -k tooling/code-graph/results/activegraph/graph.json.gz
python3 tooling/code-graph/analyze.py hubs tooling/code-graph/results/activegraph/graph.json
python3 tooling/code-graph/analyze.py calls tooling/code-graph/results/activegraph/graph.json lib
```

The results describe the commits named in `FINDINGS.md`. Line numbers drift; the graphs are cheap to rebuild.

## Regenerate

```bash
PYTHON=python3.12 tooling/code-graph/run.sh <repo-path> lib <name>
python3 tooling/code-graph/known_edges.py <graph.json> tooling/code-graph/known-edges/<name>.json
python3 -m unittest discover -s tooling/code-graph/tests
```

`run.sh` takes seconds once installed. It's macOS only, works on a clone so the target isn't written to, and stops if its sandbox or audit-hook controls fail or a socket event is logged. The audit hook sees only what Python itself does; the sandbox is what denies network to everything else. At these commits it reproduces the stored graphs byte for byte. To run the fixture, make it a repository first: copy `fixture/`, then `git init && git add -A && git commit -m fixture` in the copy, then `run.sh <copy> . fixture`.

`known_edges.py` exits 1 when a hand-verified edge disappears, and reports when a known miss or known error changes.

## What's in the branch

The commits are separate so you can drop what you don't want. `FINDINGS.md` names the tools but needs none of them to read:

| Commit | Contents | Keep it if |
|---|---|---|
| Findings | `FINDINGS.md`, this file | You want the answers |
| Stored results | `results/` | You want to query without running a tool |
| Harness | `run.sh`, lock, `audit/` | You'll regenerate graphs |
| Analysis | `analyze.py` | You'll read a graph often |
| Regression check | `known_edges.py`, `known-edges/`, `fixture/`, `tests/` | A tool upgrade or CI job should fail loudly |

## Limits

- Static only. Nothing was run against a database, and "no edge" is often the tool's blind spot, not the code's.
- One SHA per repo; samples are small and hand-read.
- `known-edges/` pins facts about one commit, so a legitimate code change can fail it. Update the file when that happens.
