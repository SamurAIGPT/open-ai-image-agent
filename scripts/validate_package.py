#!/usr/bin/env python3
"""Validate the portable image-agent skill pack without third-party packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CAPABILITIES = {
    "media.generate_image",
    "media.edit_image",
    "media.upload_file",
    "media.upscale",
    "media.enhance_image",
    "media.check_result",
    "media.search_models",
    "media.account_balance",
}

REQUIRED_FILES = (
    "AGENTS.md",
    "MODELS.md",
    "README.md",
    "references/agent-installation.md",
    "references/creative-qa.md",
    "references/muapi-image-tools.md",
    "references/reports-and-receipts.md",
)


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter start")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("missing frontmatter end")
    return text[4:end]


def main() -> int:
    errors: list[str] = []
    readme = (ROOT / "README.md").read_text()

    for required_file in REQUIRED_FILES:
        if not (ROOT / required_file).exists():
            errors.append(f"missing {required_file}")

    skills = sorted((ROOT / "agents").glob("*/SKILL.md"))
    expected_slugs = {
        "ad-creative",
        "brand-content",
        "image-editing",
        "image-enhancement",
        "image-generation",
        "image-project-setup",
        "image-strategist",
        "product-imagery",
        "social-pack",
        "thumbnail-generation",
    }
    actual_slugs = {skill.parent.name for skill in skills}
    if actual_slugs != expected_slugs:
        errors.append(
            f"expected skill directories {sorted(expected_slugs)}, found {sorted(actual_slugs)}"
        )

    for skill_file in skills:
        try:
            text = skill_file.read_text()
            metadata = frontmatter(text)
        except ValueError as exc:
            errors.append(f"{skill_file}: {exc}")
            continue

        for field in ("name:", "slug:", "version:", "status:", "permissions:"):
            if field not in metadata:
                errors.append(f"{skill_file}: missing {field}")

        slug_match = re.search(r"^slug:\s*([a-z0-9-]+)\s*$", metadata, re.MULTILINE)
        if not slug_match:
            continue
        slug = slug_match.group(1)
        if slug != skill_file.parent.name:
            errors.append(f"{skill_file}: slug does not match directory {skill_file.parent.name}")
        if f"agents/{slug}/SKILL.md" not in readme:
            errors.append(f"{skill_file}: README does not link agents/{slug}/SKILL.md")

        capability_names = re.findall(
            r"^\s+-\s+(media\.[a-z_]+)\s*$", metadata, re.MULTILINE
        )
        for capability in capability_names:
            if capability not in CAPABILITIES:
                errors.append(f"{skill_file}: unknown capability {capability}")

        if "../../MODELS.md" not in text and slug not in {
            "image-project-setup",
            "image-strategist",
        }:
            errors.append(f"{skill_file}: missing relative MODELS.md reference")

    for reference in (
        "references/muapi-image-tools.md",
        "references/creative-qa.md",
        "references/reports-and-receipts.md",
    ):
        if reference not in readme:
            errors.append(f"README does not link {reference}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skills)} image skills and {len(CAPABILITIES)} logical capabilities.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
