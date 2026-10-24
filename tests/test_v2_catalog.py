import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V2 = ROOT / "v2"


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        raise AssertionError(f"Missing YAML frontmatter: {path}")
    fields = {}
    current_list = None
    for line in match.group(1).splitlines():
        item = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if item:
            key, value = item.groups()
            if value:
                value = value.strip()
                if value.startswith('"') and value.endswith('"'):
                    value = json.loads(value)
                fields[key] = value
                current_list = None
            else:
                fields[key] = []
                current_list = key
        elif current_list and re.match(r"^\s+-\s+", line):
            value = re.sub(r"^\s+-\s+", "", line).strip()
            fields[current_list].append(value.strip('"'))
    return fields


class V2CatalogTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((V2 / "manifest.json").read_text(encoding="utf-8"))
        self.folders = {folder["key"]: folder for folder in self.manifest["folders"]}

    def test_v2_has_exactly_four_role_agents(self):
        files = self.folders["agents"]["files"]
        self.assertEqual(len(files), 4)
        names = [parse_frontmatter(ROOT / self.folders["agents"]["path"] / name)["name"] for name in files]
        self.assertEqual(names, ["Developer", "Documentation Analyst", "QA Engineer", "Automation QA Engineer"])

    def test_each_agent_references_existing_reusable_skills(self):
        skill_folder = self.folders["skills"]
        skill_ids = {Path(path).parts[0] for path in skill_folder["files"]}
        self.assertGreaterEqual(len(skill_ids), 50, "v2 must retain its current skill catalogue while allowing user additions")
        linked_skill_ids = set()
        for filename in self.folders["agents"]["files"]:
            metadata = parse_frontmatter(ROOT / self.folders["agents"]["path"] / filename)
            self.assertTrue(metadata.get("skills"), f"No skills linked from {filename}")
            self.assertTrue(set(metadata["skills"]).issubset(skill_ids), filename)
            linked_skill_ids.update(metadata["skills"])
        self.assertEqual(skill_ids, linked_skill_ids, "Every v2 skill must be listed by at least one role agent")

    def test_skills_follow_agent_skills_names_and_description_limits(self):
        folder = self.folders["skills"]
        for relative_path in folder["files"]:
            skill_path = ROOT / folder["path"] / relative_path
            metadata = parse_frontmatter(skill_path)
            slug = Path(relative_path).parts[0]
            name = metadata["name"]
            description = metadata["description"]
            self.assertEqual(name, slug)
            self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
            self.assertLessEqual(len(name), 64)
            self.assertGreaterEqual(len(description), 1)
            self.assertLessEqual(len(description), 1024)

    def test_m365_profiles_mirror_four_roles_with_five_prompts(self):
        data = json.loads((V2 / "m365-agents.json").read_text(encoding="utf-8"))
        agents = data["agents"]
        self.assertEqual(len(agents), 4)
        expected_names = {"Developer", "Documentation Analyst", "QA Engineer", "Automation QA Engineer"}
        self.assertEqual({agent["name"] for agent in agents}, expected_names)
        for agent in agents:
            self.assertLessEqual(len(agent["name"]), 30)
            self.assertGreater(len(agent["description"]), 0)
            self.assertLessEqual(len(agent["description"]), 1000)
            self.assertGreater(len(agent["instructionPrompt"]), 0)
            self.assertLessEqual(len(agent["instructionPrompt"]), 8000)
            self.assertEqual(len(agent["promptTemplates"]), 5)
            self.assertTrue(all(prompt.get("title") and prompt.get("text") for prompt in agent["promptTemplates"]))
            self.assertIn("Tasks you can perform:", agent["instructionPrompt"])
            self.assertNotIn("skill", agent["instructionPrompt"].lower())

    def test_role_profiles_are_concise_platform_neutral_skill_selectors(self):
        folder = self.folders["agents"]
        for filename in folder["files"]:
            metadata = parse_frontmatter(ROOT / folder["path"] / filename)
            self.assertLessEqual(len(metadata["description"]), 200)
            self.assertTrue(metadata.get("skills"))
            body = (ROOT / folder["path"] / filename).read_text(encoding="utf-8").split("---", 2)[-1]
            self.assertIn("select the best-matching listed skill", body.lower())
            self.assertNotIn("copilot", body.lower())

    def test_project_context_skill_mentions_both_requested_locations(self):
        context = (V2 / "Skills/project-context/SKILL.md").read_text(encoding="utf-8")
        self.assertIn(".vscode/", context)
        self.assertIn(".copilot/", context)

    def test_markdown_renderers_escape_untrusted_text(self):
        for filename in ("index.html", "v1.html"):
            html = (ROOT / filename).read_text(encoding="utf-8")
            inline = re.search(r"function inlineFormat\(text\)\s*\{([\s\S]*?)\n  \}", html)
            self.assertIsNotNone(inline, filename)
            formatter_body = inline.group(1) if inline else ""
            self.assertTrue(formatter_body.lstrip().startswith("text = escapeHtml(text);"), filename)
            self.assertIn("inlineFormat(cb[2])", html, filename)
            self.assertIn('data-skill-id="${escapeHtml(skill.id)}"', html, filename)

    def test_version_switch_and_m365_subpage_are_in_the_app(self):
        v1 = (ROOT / "v1.html").read_text(encoding="utf-8")
        self.assertIn('data-target="v1.html"', (ROOT / "index.html").read_text(encoding="utf-8"))
        self.assertIn('data-target="index.html"', v1)
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="version-toggle"', html)
        self.assertIn('role="switch"', html)
        self.assertIn("v1.0", html.lower())
        self.assertIn("v2.0", html.lower())
        self.assertIn('id="m365-page"', html)


if __name__ == "__main__":
    unittest.main()
