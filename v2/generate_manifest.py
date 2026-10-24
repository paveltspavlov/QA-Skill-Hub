#!/usr/bin/env python3
"""Rebuild the v2 catalogue manifest from v2 role and Agent Skill files.

Add a project-neutral role profile to v2/Agents/ or a skill directory at
v2/Skills/<skill-name>/SKILL.md, then run this script. The legacy prompt set
remains sourced from the v1 manifest so v1 content is not modified.
"""
from __future__ import annotations

import json
from pathlib import Path

V2 = Path(__file__).resolve().parent
ROOT = V2.parent
MANIFEST = V2 / "manifest.json"
LEGACY_MANIFEST = ROOT / "manifest.json"

AGENT_ORDER = [
    "developer.md",
    "documentation-analyst.md",
    "qa-engineer.md",
    "automation-qa-engineer.md",
]

FOLDERS = [
    {
        "key": "agents",
        "label": "Agents",
        "path": "v2/Agents",
        "blurb": "Four concise, cross-platform roles that select reusable skills for each task.",
    },
    {
        "key": "skills",
        "label": "Skills",
        "path": "v2/Skills",
        "blurb": "Reusable, task-specific Agent Skills that can be selected by more than one role.",
    },
    {
        "key": "prompts",
        "label": "Prompts",
        "path": "Prompts",
        "blurb": "The existing standalone prompt catalogue, retained for continuity.",
    },
]


def preserve_order(previous: dict, key: str, items: list[str]) -> list[str]:
    old = previous.get(key, [])
    return [item for item in old if item in items] + [item for item in items if item not in old]


def order_agents(items: list[str]) -> list[str]:
    return [name for name in AGENT_ORDER if name in items] + [name for name in items if name not in AGENT_ORDER]


def main() -> None:
    old_manifest = json.loads(LEGACY_MANIFEST.read_text(encoding="utf-8"))
    prompt_folder = next(folder for folder in old_manifest["folders"] if folder["key"] == "prompts")
    previous = {}
    if MANIFEST.exists():
        try:
            previous = {
                folder["key"]: folder.get("files", [])
                for folder in json.loads(MANIFEST.read_text(encoding="utf-8")).get("folders", [])
            }
        except (ValueError, KeyError, TypeError):
            previous = {}

    found = {
        "agents": sorted(path.name for path in (V2 / "Agents").glob("*.md")),
        "skills": sorted(
            path.relative_to(V2 / "Skills").as_posix()
            for path in (V2 / "Skills").glob("*/SKILL.md")
        ),
        "prompts": prompt_folder["files"],
    }
    result = {
        "version": "2.0",
        "generated": "by v2/generate_manifest.py",
        "folders": [],
    }
    for folder in FOLDERS:
        result["folders"].append({
            **folder,
            "files": order_agents(found["agents"]) if folder["key"] == "agents" else preserve_order(previous, folder["key"], found[folder["key"]]),
        })
    MANIFEST.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Rebuilt v2/manifest.json")
    for folder in result["folders"]:
        print(f"  {folder['label']}: {len(folder['files'])}")


if __name__ == "__main__":
    main()
