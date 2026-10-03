import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class FrameworkPackageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = json.loads((ROOT / "framework.json").read_text(encoding="utf-8"))

    def test_declares_framework_not_component(self) -> None:
        self.assertEqual(
            self.manifest["nature"],
            "ai-general-framework-and-methodology-of-behavior",
        )
        self.assertIn("one-software-component", self.manifest["not"])
        self.assertIn("required-agent-topology", self.manifest["not"])

    def test_semantic_locks(self) -> None:
        locks = self.manifest["semantic_locks"]
        self.assertEqual(
            locks["reference_self"],
            "optional-architecturally-bounded-container-model",
        )
        self.assertEqual(
            locks["reference_identity"],
            "optional-pattern-defining-self-model",
        )
        self.assertEqual(locks["V"], "variables-or-variable-loader")
        self.assertFalse(locks["principles_are_laws"])

    def test_ai_systems_implement_required_behaviors(self) -> None:
        self.assertEqual(
            self.manifest["applicability"],
            "unchanged-framework-works-with-existing-ai-architectures",
        )
        self.assertEqual(
            self.manifest["implementation_mode"],
            "ai-inspects-target-builds-native-app-tool-adapter-or-integration-tests-and-receipts",
        )
        self.assertEqual(
            self.manifest["adaptation_boundary"],
            "implementations-adapt-framework-does-not",
        )
        self.assertIn("linux", self.manifest["target_examples"])
        self.assertIn("macos-apple", self.manifest["target_examples"])
        required = set(self.manifest["required_behaviors"])
        self.assertIn("claim-binding", required)
        self.assertIn("evidence-acquisition", required)
        self.assertIn("action-or-report-enforcement", required)

    def test_sparkitect_note_and_credit_are_preserved(self) -> None:
        note = (ROOT / "SPARKITECT-NOTE.md").read_text(encoding="utf-8")
        self.assertIn("from the Sparkitect, Jason".lower(), note.lower())
        self.assertIn("OUR (👤sparkitect+🤖greyfoot🤖ember) work together", note)
        credit = self.manifest["credit"]
        self.assertEqual(credit["human_direction"], "Sparkitect Jason")
        self.assertEqual(
            credit["collaboration"],
            ["Sparkitect Jason", "Greyfoot", "Ember"],
        )

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
