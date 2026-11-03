"""python3 -m unittest discover -s tooling/code-graph/tests"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import analyze  # noqa: E402
import known_edges  # noqa: E402

GRAPH = {
    "nodes": [
        {"id": "a", "label": "A", "source_file": "a.rb"},
        {"id": "b", "label": "B", "source_file": "b.rb"},
        {"id": "m", "label": ".m()", "source_file": "a.rb"},
    ],
    "links": [
        {"source": "a", "target": "b", "relation": "mixes_in", "confidence": "EXTRACTED"},
        {"source": "a", "target": "m", "relation": "method", "confidence": "EXTRACTED"},
    ],
}


class KnownEdges(unittest.TestCase):
    def run_cli(self, expectations):
        with tempfile.TemporaryDirectory() as tmp:
            graph_path, expect_path = os.path.join(tmp, "g.json"), os.path.join(tmp, "e.json")
            with open(graph_path, "w") as f:
                json.dump(GRAPH, f)
            with open(expect_path, "w") as f:
                json.dump(expectations, f)
            return subprocess.run(
                [sys.executable, os.path.join(ROOT, "known_edges.py"), graph_path, expect_path],
                capture_output=True, text=True,
            )

    def test_present_edge_passes(self):
        result = self.run_cli({"must_have": [{"relation": "mixes_in", "source": "A", "target": "B"}]})
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_absent_edge_fails(self):
        result = self.run_cli({"must_have": [{"relation": "mixes_in", "source": "B", "target": "A"}]})
        self.assertEqual(result.returncode, 1)
        self.assertIn("MISSING B --mixes_in--> A", result.stdout)

    def test_file_filter_can_reject(self):
        want = {"relation": "mixes_in", "source": "A", "source_file": "other.rb", "target": "B"}
        self.assertEqual(self.run_cli({"must_have": [want]}).returncode, 1)

    def test_empty_must_have_is_refused(self):
        self.assertEqual(self.run_cli({"must_have": []}).returncode, 2)

    def test_non_object_input_is_refused_not_reported_as_a_miss(self):
        self.assertEqual(self.run_cli(["not", "an", "object"]).returncode, 2)

    def test_news_is_reported_but_passes(self):
        result = self.run_cli({
            "must_have": [{"relation": "mixes_in", "source": "A", "target": "B"}],
            "known_missing": [{"relation": "method", "source": "A", "target": ".m()"}],
            "known_wrong": [{"relation": "calls", "source": "A", "target": "B"}],
        })
        self.assertEqual(result.returncode, 0)
        self.assertIn("now present", result.stdout)
        self.assertIn("now gone", result.stdout)


class CallForm(unittest.TestCase):
    def test_forms(self):
        cases = [
            ("B", "B.new", "class reference"),
            (".m()", "m(1)", "implicit self"),
            (".m()", "self.m", "self."),
            (".m()", "Foo::Bar.m(1)", "Constant."),
            (".m()", "@thing.m", "explicit receiver"),
            (".m()", "other_call", "not on this line"),
        ]
        for label, line, expected in cases:
            self.assertEqual(analyze.call_form({}, label, line), expected, line)


if __name__ == "__main__":
    unittest.main()
