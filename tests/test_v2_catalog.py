import json
import re
import shutil
import subprocess
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

    def test_qa_role_descriptions_name_concrete_deliverables(self):
        qa_path = V2 / "Agents/qa-engineer.md"
        role = parse_frontmatter(qa_path)
        expected = ("traceable test cases", "risk-ranked regression plans", "reproducible defect reports", "coverage gaps")
        for phrase in expected:
            self.assertIn(phrase, role["description"].lower())
        m365 = json.loads((V2 / "m365-agents.json").read_text(encoding="utf-8"))
        qa_m365 = next(agent for agent in m365["agents"] if agent["id"] == "qa-engineer")
        for phrase in expected:
            self.assertIn(phrase, qa_m365["description"].lower())

    def test_each_agent_references_existing_reusable_skills(self):
        skill_folder = self.folders["skills"]
        skill_ids = {Path(path).parts[0] for path in skill_folder["files"]}
        self.assertGreaterEqual(len(skill_ids), 62, "v2 must include the expanded catalogue and allow user additions")
        linked_skill_ids = set()
        for filename in self.folders["agents"]["files"]:
            metadata = parse_frontmatter(ROOT / self.folders["agents"]["path"] / filename)
            self.assertTrue(metadata.get("skills"), f"No skills linked from {filename}")
            self.assertIn("evidence-readiness-gate", metadata["skills"], filename)
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

    def test_v1_agent_workflows_are_available_as_reusable_v2_skills(self):
        skill_ids = {Path(path).parts[0] for path in self.folders["skills"]["files"]}
        required = {
            "ai-test-strategy", "commit-message-writer", "database-migration-generator",
            "dependency-updater", "e2e-test-architecture", "environment-config-auditor",
            "error-handling-auditor", "file-scaffolder", "performance-test-planner",
            "pull-request-description-writer", "release-notes-writer", "evidence-readiness-gate",
        }
        self.assertTrue(required.issubset(skill_ids), f"Missing restored workflows: {sorted(required - skill_ids)}")

    def test_every_skill_has_deliverable_quality_and_uncertainty_contracts(self):
        folder = self.folders["skills"]
        for relative_path in folder["files"]:
            text = (ROOT / folder["path"] / relative_path).read_text(encoding="utf-8")
            self.assertIn("## Required Inputs", text, relative_path)
            self.assertIn("## Procedure", text, relative_path)
            self.assertIn("## Output Contract", text, relative_path)
            self.assertIn("## Quality Gate", text, relative_path)
            self.assertIn("## Evidence and Uncertainty", text, relative_path)

    def test_role_agents_enforce_evidence_readiness_without_fake_confidence(self):
        folder = self.folders["agents"]
        for filename in folder["files"]:
            text = (ROOT / folder["path"] / filename).read_text(encoding="utf-8").lower()
            self.assertIn("75% evidence-readiness gate", text, filename)
            self.assertIn("not a probability", text, filename)
            self.assertRegex(text, r"(?:do not invent|never invent)", filename)
            self.assertIn("output contract", text, filename)

    def test_m365_profiles_include_quality_gate_without_skills(self):
        data = json.loads((V2 / "m365-agents.json").read_text(encoding="utf-8"))
        for agent in data["agents"]:
            prompt = agent["instructionPrompt"].lower()
            self.assertIn("75% evidence-readiness gate", prompt, agent["name"])
            self.assertIn("not a probability", prompt, agent["name"])
            self.assertIn("do not invent", prompt, agent["name"])
            self.assertNotIn("skill", prompt, agent["name"])

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
            self.assertIn("tasks you can perform:", agent["instructionPrompt"].lower())
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

    def test_markdown_renderers_escape_untrusted_html_at_runtime(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("Node.js is needed for the optional runtime renderer check")
        payload = '<img src=x onerror=alert(1)> **safe**'
        newline = chr(10)
        for filename in ("index.html", "v1.html"):
            html = (ROOT / filename).read_text(encoding="utf-8")
            functions = []
            for name in ("escapeHtml", "inlineFormat"):
                marker = "  function " + name + "("
                function_start = html.find(marker)
                self.assertNotEqual(function_start, -1, filename)
                function_end = html.find(newline + "  }", function_start)
                self.assertNotEqual(function_end, -1, filename)
                functions.append(html[function_start:function_end + len(newline + "  }")])
            source = newline.join(functions)
            program = (
                "const src=" + json.dumps(source) + ";"
                "const format=new Function(src+String.fromCharCode(10)+'return inlineFormat')();"
                "process.stdout.write(format(require('fs').readFileSync(0,'utf8')));"
            )
            result = subprocess.run([node, "-e", program], input=payload, text=True, capture_output=True, check=True)
            self.assertIn("&lt;img", result.stdout, filename)
            self.assertNotIn("<img", result.stdout, filename)
            self.assertIn("<strong>safe</strong>", result.stdout, filename)

    def test_research_sources_preserve_verbatim_openai_quote(self):
        source_note = (V2 / "RESEARCH-SOURCES.md").read_text(encoding="utf-8")
        quote = (
            '> "Structured Outputs is a feature that ensures the model will always generate responses '
            'that adhere to your supplied JSON Schema, so you don’t need to worry about the model '
            'omitting a required key, or hallucinating an invalid enum value."'
        )
        self.assertIn(quote, source_note)

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
