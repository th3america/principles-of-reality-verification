"""Validate the public framework package without claiming semantic truth."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_COMPONENTS = {
    "ontology",
    "principles",
    "rules",
    "invariants",
    "models",
    "methodologies",
    "architecture-patterns",
    "mechanism-patterns",
    "tests",
    "resolution-surfaces",
    "receipts",
    "failure-taxonomy",
    "implementation-guides",
    "tools-and-implementations",
}

FORBIDDEN_TEXT = (
    "C:\\Users\\",
    "App" + "Data\\",
    "api" + "_key=",
    "authorization:" + " bearer",
)


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    manifest_path = root / "framework.json"
    if not manifest_path.is_file():
        return ["missing framework.json"]

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalid framework.json: {exc}"]

    if manifest.get("protocol") != "PrinciplesOfRealityVerification/1":
        errors.append("unexpected protocol")

    components = set(manifest.get("components", []))
    missing_components = sorted(REQUIRED_COMPONENTS - components)
    if missing_components:
        errors.append(f"missing components: {', '.join(missing_components)}")

    for relative in manifest.get("documents", []):
        path = root / relative
        if not path.is_file():
            errors.append(f"missing document: {relative}")

    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".json", ".py", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8")
        for forbidden in FORBIDDEN_TEXT:
            if forbidden.lower() in text.lower():
                errors.append(f"private/sensitive pattern in {path.relative_to(root)}: {forbidden}")

    return errors


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).parent
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: framework package structure and public-boundary scan")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
