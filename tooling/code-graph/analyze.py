#!/usr/bin/env python3
"""Read a Graphify graph.json with the corrections FINDINGS.md says it needs.

  analyze.py shares GRAPH            edge shares by relation and confidence
  analyze.py hubs GRAPH [N]          hubs ranked without method/contains edges
  analyze.py calls GRAPH SOURCE      calls grouped by how the call is written
  analyze.py mixins GRAPH SOURCE     include/extend/prepend lines with no edge

SOURCE is the directory Graphify was pointed at (run.sh prints it). Standard
library only.
"""
import collections
import json
import os
import re
import sys

STRUCTURAL = {"method", "contains"}


def load(path):
    with open(path) as f:
        graph = json.load(f)
    return graph, {n["id"]: n for n in graph["nodes"]}, graph["links"]


def source_line(source, edge, cache):
    match = re.match(r"L(\d+)", str(edge.get("source_location") or ""))
    path = os.path.join(source, edge.get("source_file") or "")
    if not match or not os.path.isfile(path):
        return ""
    if path not in cache:
        with open(path, errors="replace") as f:
            cache[path] = f.read().split("\n")
    return cache[path][int(match.group(1)) - 1]


def shares(path):
    _, _, edges = load(path)
    total = len(edges)
    structural = sum(e["relation"] in STRUCTURAL for e in edges)
    calls = [e for e in edges if e["relation"] == "calls"]
    inferred_calls = sum(e["confidence"] == "INFERRED" for e in calls)
    print(f"edges {total}; method+contains {100 * structural / total:.1f}%")
    print(f"calls {len(calls)}; INFERRED {100 * inferred_calls / max(len(calls), 1):.1f}%")
    counts = collections.Counter((e["relation"], e["confidence"]) for e in edges)
    for (relation, confidence), count in counts.most_common():
        print(f"  {count:6d} {relation} {confidence}")


def hubs(path, top=15):
    _, nodes, edges = load(path)
    degree = collections.defaultdict(collections.Counter)
    for e in edges:
        degree[e["source"]][e["relation"]] += 1
        degree[e["target"]][e["relation"]] += 1
    # A node with no source file is an unresolved superclass name, not a hub.
    rank = sorted(
        ((node, relations) for node, relations in degree.items() if nodes[node].get("source_file")),
        key=lambda kv: -sum(v for k, v in kv[1].items() if k not in STRUCTURAL),
    )
    for node, relations in rank[:top]:
        coupling = sum(v for k, v in relations.items() if k not in STRUCTURAL)
        print(f"{coupling:5d} {nodes[node]['label']} {nodes[node].get('source_file')} {dict(relations)}")


def call_form(edge, label, line):
    """How a call is written, which is what predicts whether its edge is right."""
    if not label.startswith("."):
        return "class reference"
    name = re.sub(r"^\.|\(\)$", "", label)
    receiver = re.search(r"([\w:@\]\)\}\?!\"']+)\s*&?\.\s*" + re.escape(name) + r"\b", line)
    if not receiver:
        return "implicit self" if re.search(r"\b" + re.escape(name) + r"\b", line) else "not on this line"
    text = receiver.group(1)
    if text == "self":
        return "self."
    return "Constant." if re.match(r"^(::)?[A-Z]", text) else "explicit receiver"


def calls(path, source):
    _, nodes, edges = load(path)
    cache = {}
    forms = collections.Counter()
    for e in edges:
        if e["relation"] != "calls":
            continue
        line = source_line(source, e, cache)
        same = nodes[e["source"]].get("source_file") == nodes[e["target"]].get("source_file")
        forms[(call_form(e, nodes[e["target"]]["label"], line), e["confidence"], "same file" if same else "cross file")] += 1
    for key, count in forms.most_common():
        print(f"{count:6d} {' | '.join(key)}")


def mixins(path, source):
    _, nodes, edges = load(path)
    have = {(e.get("source_file"), e.get("source_location")) for e in edges if e["relation"] == "mixes_in"}
    labels = collections.Counter(n["label"] for n in nodes.values() if n.get("source_file"))
    hit = external = 0
    missed = []
    for root, _, names in os.walk(source):
        for name in names:
            if not name.endswith(".rb"):
                continue
            full = os.path.join(root, name)
            rel = os.path.relpath(full, source)
            with open(full, errors="replace") as f:
                for number, text in enumerate(f, 1):
                    match = re.match(r"\s*(include|extend|prepend)\s+(::)?([A-Z][\w:]*)", text)
                    if not match:
                        continue
                    if (rel, f"L{number}") in have:
                        hit += 1
                    elif labels.get(match.group(3), 0) or any(k.endswith("::" + match.group(3)) for k in labels):
                        missed.append((rel, number, match.group(3), labels.get(match.group(3), 0)))
                    else:
                        external += 1
    print(f"edge {hit}; target not in this code {external}; target here but no edge {len(missed)}")
    for rel, number, target, count in missed:
        print(f"  {rel}:{number} {target} ({count} nodes with this label)")


def main(argv):
    commands = {"shares": (shares, 1), "hubs": (hubs, 1), "calls": (calls, 2), "mixins": (mixins, 2)}
    if len(argv) < 2 or argv[0] not in commands or len(argv) - 1 < commands[argv[0]][1]:
        print(__doc__, file=sys.stderr)
        return 2
    function, _ = commands[argv[0]]
    if argv[0] == "hubs" and len(argv) > 2:
        hubs(argv[1], int(argv[2]))
    else:
        function(*argv[1:])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
