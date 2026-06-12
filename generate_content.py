#!/usr/bin/env python3
"""Generate the Agents/ Skills/ Prompts/ content folders and manifest.json.

Source of truth for the *initial* migration is the embedded `#skill-data`
JSON block in index.html. After this runs, the .md files in the three folders
become the source of truth: add a new .md file, add its name to manifest.json,
and the app will render it on the next load.

Each generated .md file has a small YAML frontmatter block followed by the
markdown body. The frontmatter is the "YAML format" users copy into GitHub
Copilot / Claude skill files. The body is the full reference shown in the card.

Folder mapping (re-map of the old sections):
    agent                 -> Agents
    qa, dev, mcp          -> Skills
    qa-prompts, dev-prompts -> Prompts
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, "index.html")

FOLDERS = [
    {"key": "agents", "label": "Agents", "path": "Agents",
     "blurb": "Autonomous, multi-step agents that take action across your codebase."},
    {"key": "skills", "label": "Skills", "path": "Skills",
     "blurb": "Focused, reusable skills that produce a specific deliverable on demand."},
    {"key": "prompts", "label": "Prompts", "path": "Prompts",
     "blurb": "Ready-to-paste prompts for one-off tasks in Copilot or Claude Chat."},
]

# old section -> folder key
SECTION_TO_FOLDER = {
    "agent": "agents",
    "qa": "skills",
    "dev": "skills",
    "mcp": "skills",
    "qa-prompts": "prompts",
    "dev-prompts": "prompts",
}


def load_skills():
    html = open(INDEX, encoding="utf-8").read()
    m = re.search(r'<script id="skill-data"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        raise SystemExit("Could not find #skill-data block in index.html")
    return json.loads(m.group(1))


def yaml_dq(s):
    """Double-quote a scalar for YAML, escaping backslashes and quotes."""
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    # frontmatter scalars must stay on one line
    s = s.replace("\n", " ").replace("\r", " ")
    return '"' + s + '"'


def frontmatter(skill, folder_key):
    lines = ["---"]
    lines.append("id: " + skill["id"])
    lines.append("name: " + yaml_dq(skill["name"]))
    lines.append("folder: " + folder_key)
    # keep the original sub-section as a hint for search / future grouping
    lines.append("section: " + skill.get("section", ""))
    lines.append("summary: " + yaml_dq(skill["summary"]))
    for field in ("istqbTopics", "aiTools", "tags"):
        vals = skill.get(field) or []
        if vals:
            lines.append(field + ":")
            for v in vals:
                lines.append("  - " + yaml_dq(str(v)))
    lines.append("---")
    return "\n".join(lines)


def write_manifest(files):
    manifest = {
        "generated": "by generate_content.py",
        "folders": [
            {
                "key": f["key"],
                "label": f["label"],
                "path": f["path"],
                "blurb": f["blurb"],
                "files": files[f["key"]],
            }
            for f in FOLDERS
        ],
    }
    with open(os.path.join(HERE, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)


def scan():
    """Rebuild manifest.json from whatever .md files currently live in the
    three folders. Run this after you add/remove a .md file by hand. Existing
    curated order is preserved; brand-new files are appended (sorted); files
    that no longer exist are dropped."""
    prev = {}
    mpath = os.path.join(HERE, "manifest.json")
    if os.path.exists(mpath):
        try:
            data = json.load(open(mpath, encoding="utf-8"))
            for fo in data.get("folders", []):
                prev[fo["key"]] = fo.get("files", [])
        except (ValueError, KeyError):
            pass

    files = {}
    for f in FOLDERS:
        folder_dir = os.path.join(HERE, f["path"])
        os.makedirs(folder_dir, exist_ok=True)
        on_disk = sorted(
            os.path.basename(p) for p in glob.glob(os.path.join(folder_dir, "*.md"))
        )
        ordered = [fn for fn in prev.get(f["key"], []) if fn in on_disk]
        ordered += [fn for fn in on_disk if fn not in ordered]
        files[f["key"]] = ordered

    write_manifest(files)
    print("[+] Rebuilt manifest.json from folder contents")
    for f in FOLDERS:
        print(f"    {f['label']:8} {len(files[f['key']]):3} files")


def main():
    skills = load_skills()
    counts = {f["key"]: 0 for f in FOLDERS}
    files = {f["key"]: [] for f in FOLDERS}

    for f in FOLDERS:
        os.makedirs(os.path.join(HERE, f["path"]), exist_ok=True)

    for skill in skills:
        folder_key = SECTION_TO_FOLDER.get(skill.get("section"), "skills")
        folder = next(f for f in FOLDERS if f["key"] == folder_key)
        fname = skill["id"] + ".md"
        body = skill.get("detailMd", "").rstrip("\n")
        content = frontmatter(skill, folder_key) + "\n\n" + body + "\n"
        with open(os.path.join(HERE, folder["path"], fname), "w", encoding="utf-8") as fh:
            fh.write(content)
        files[folder_key].append(fname)
        counts[folder_key] += 1

    write_manifest(files)

    total = sum(counts.values())
    print(f"[+] Wrote {total} files")
    for f in FOLDERS:
        print(f"    {f['label']:8} {counts[f['key']]:3} -> {f['path']}/")
    print("[+] Wrote manifest.json")


if __name__ == "__main__":
    if "--scan" in sys.argv:
        scan()
    else:
        main()
