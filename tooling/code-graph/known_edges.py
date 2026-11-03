#!/usr/bin/env python3
"""Check a Graphify graph.json against edges a person has read in the source.

  known_edges.py GRAPH EXPECTATIONS.json

EXPECTATIONS holds three lists of {relation, source, target}, each optionally
with source_file and target_file (substrings), and a note:

  must_have      read and correct. Absent means the tool or the code changed:
                 exit 1, so a silent extractor regression turns red.
  known_missing  real in the source, absent from the graph. Showing up is
                 news, reported but not a failure.
  known_wrong    in the graph, false in the source. Disappearing is news, too.

Exit 0 when every must_have edge is present, 1 when one is not, 2 on bad input.
Standard library only.
"""
import json
import sys


def present(want, nodes, edges):
    def matches(node_id, label, file_part):
        node = nodes[node_id]
        return node["label"] == label and (not file_part or file_part in str(node.get("source_file")))

    return any(
        e["relation"] == want["relation"]
        and matches(e["source"], want["source"], want.get("source_file"))
        and matches(e["target"], want["target"], want.get("target_file"))
        for e in edges
    )


def describe(want):
    return f"{want['source']} --{want['relation']}--> {want['target']}"


def check(graph, expectations):
    nodes = {n["id"]: n for n in graph["nodes"]}
    edges = graph["links"]
    missing = [w for w in expectations["must_have"] if not present(w, nodes, edges)]
    appeared = [w for w in expectations.get("known_missing", []) if present(w, nodes, edges)]
    gone = [w for w in expectations.get("known_wrong", []) if not present(w, nodes, edges)]
    return missing, appeared, gone


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    try:
        with open(argv[0]) as f:
            graph = json.load(f)
        with open(argv[1]) as f:
            expectations = json.load(f)
        if not expectations["must_have"]:
            raise ValueError("must_have is empty, so this check could not fail")
        missing, appeared, gone = check(graph, expectations)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(f"known_edges: {error!r}", file=sys.stderr)
        return 2
    print(f"must_have {len(expectations['must_have']) - len(missing)}/{len(expectations['must_have'])} present")
    for want in missing:
        print(f"MISSING {describe(want)}")
    for want in appeared:
        print(f"now present (was known_missing): {describe(want)}")
    for want in gone:
        print(f"now gone (was known_wrong): {describe(want)}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
