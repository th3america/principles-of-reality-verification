import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class FrameworkPackageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = json.loads((ROOT / "framework.json").read_text(encoding="utf-8"))

    def test_declares_framework_not_component(self) -> None:
        self.assertEqual(self.manifest["nature"], "framework-and-methodology-of-behavior")
        self.assertIn("one-software-component", self.manifest["not"])

    def test_semantic_locks(self) -> None:
        locks = self.manifest["semantic_locks"]
        self.assertEqual(locks["self"], "architecturally-bounded-container")
        self.assertEqual(locks["identity"], "pattern-defining-self")
        self.assertEqual(locks["V"], "variables-or-variable-loader")
        self.assertFalse(locks["principles_are_laws"])

    def test_documents_exist(self) -> None:
        for relative in self.manifest["documents"]:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_private_material_is_excluded(self) -> None:
        boundary = self.manifest["public_boundary"]
        self.assertFalse(boundary["private_workbench_included"])
        self.assertFalse(boundary["raw_conversations_included"])
        self.assertFalse(boundary["local_paths_included"])
        self.assertFalse(boundary["credentials_included"])


if __name__ == "__main__":
    unittest.main()
