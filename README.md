# QA Skill Hub

A single-page web app that showcases a catalogue of ready-to-use AI **Agents**,
**Skills**, and **Prompts** for QA and development work. Each item can be expanded
to read its full reference, and copied — either as the original Markdown or as the
YAML frontmatter you paste into a GitHub Copilot / Claude skill file.

The content is **not** hard-coded in the page. It lives as individual Markdown
files inside three folders, and the app loads them at runtime. Add a file, refresh,
and it shows up.

---

## Repository layout

```
.
├── index.html            # the app (HTML + CSS + JS, no build step)
├── manifest.json         # lists which .md files belong to each folder
├── generate_content.py   # tooling to (re)generate files and rebuild the manifest
├── Agents/               # one .md per Agent
├── Skills/               # one .md per Skill
└── Prompts/              # one .md per Prompt
```

Each `.md` file has a small **YAML frontmatter** block followed by a **Markdown body**:

```markdown
---
id: commit-message-writer
name: "Commit Message Writer"
folder: agents
section: agent
summary: "Analyzes staged git changes and writes a Conventional Commits message."
tags:
  - "git"
  - "commits"
---

# Commit Message Writer

## Role
...the full reference body in Markdown...
```

- The **frontmatter** is what the app shows under the *YAML* toggle and what you
  copy into a Copilot/Claude skill file's header.
- The **body** (everything after the second `---`) is the full reference shown
  in the expanded card and copied under the *Markdown* toggle.

---

## Running the app

The page reads the `Agents/`, `Skills/`, and `Prompts/` folders over HTTP, so it
**must be served by a web server**. Opening `index.html` directly from disk
(`file://`) is blocked by the browser, and the page will tell you so.

From the project root:

```bash
python -m http.server 8000
```

Then open <http://localhost:8000/>.

Any static file server works (`npx serve`, nginx, GitHub Pages, etc.) — the app is
plain static files with no build step.

---

## Using the app

- **Browse** the three sections: **Agents**, **Skills**, **Prompts**.
- **Filter** with the **Type** pills (All / Agents / Skills / Prompts / MCP)
  and the **Role** pills (All / QA / DEV), or **search** by name, summary, tag,
  or any text in the body. The **MCP** pill shows the Model Context Protocol
  explainer plus the MCP-tagged skills. The role comes from each file's
  `roles` frontmatter list when present, otherwise from its `section`
  (`qa*` → QA, `dev*` / `mcp` → DEV).
- **Click a card** to expand it. Inside an expanded card, toggle between:
  - **Rendered** — the body formatted for reading.
  - **Markdown** — the raw reference body.
  - **YAML** — the file's frontmatter.
  - **Copilot** — a ready-to-save GitHub Copilot prompt file
    (`description` + `mode` frontmatter followed by the body; agents get
    `mode: agent`, everything else `mode: ask`).
- **Copy** copies whichever format is currently selected (Rendered copies the
  raw Markdown).
- **Deep links** — the URL hash tracks what you're looking at:
  `#skills` selects a filter, `#skills/test-case-generator` also expands that
  card. Share the link and the recipient lands on the same view.

The landing page has a tabbed **How to Use Them** guide with the same
information per content type; selecting a filter pill switches the guide to the
matching tab.

### Where the copied content goes

The three content types are used differently:

- **Agents** — need an agentic tool, primarily **GitHub Copilot agent mode**
  (also Cursor, Claude Code). Use the card's **Copilot** toggle and save the
  result as `.github/prompts/<agent-id>.prompt.md` — it carries `mode: agent`,
  so running `/<agent-id>` in Copilot Chat gives it file and terminal access.
  For an always-on workflow, add the body to `.github/copilot-instructions.md`
  or `AGENTS.md`.
- **Skills** — install once per project. Use the **Copilot** toggle and save as
  `.github/prompts/<skill-id>.prompt.md`, then run `/<skill-id>` in Copilot
  Chat. Tools without prompt-file support can use the skill's
  *Ready-to-use prompt* block directly.
- **Prompts** — nothing to install. Copy the prompt block, replace the
  `[PLACEHOLDERS]`, and paste into any chat AI.

You can also skip the app entirely and copy the `.md` files straight from the
`Agents/`, `Skills/`, and `Prompts/` folders — the Markdown body is identical
to what the Copy button produces.

---

## Adding new content

There are two ways to add an item.

### Option A — add a file by hand (recommended)

1. Create a new `.md` file in the appropriate folder (`Agents/`, `Skills/`, or
   `Prompts/`). Name it after its `id`, e.g. `Skills/my-new-skill.md`.
2. Give it frontmatter and a body (see the format above). Minimum fields:
   `id`, `name`, `folder` (`agents` | `skills` | `prompts`), and `summary`.
   `tags`, `aiTools`, and `istqbTopics` are optional lists.
3. Refresh the browser — the new card appears in its section automatically.
   On servers that render folder indexes (`python -m http.server`, nginx
   `autoindex`, `npx serve`, …) the app reads the directory listing and picks
   up any `.md` file that isn't in the manifest yet.
4. Optionally, persist it in the manifest:

   ```bash
   python generate_content.py --scan
   ```

   This rebuilds `manifest.json` from whatever `.md` files are present. Existing
   ordering is preserved, brand-new files are appended, and deleted files are
   dropped.

> **When is `--scan` still needed?** Some static hosts (GitHub Pages, S3
> without index listings) don't expose folder contents, so the app falls back
> to `manifest.json` alone there. Run `--scan` before deploying to such a host,
> or whenever you want to control the card order (the manifest's `files` arrays
> define it).

### Option B — regenerate everything

`generate_content.py` (with no flags) regenerates **all** content files and the
manifest from the embedded catalogue. This was used for the initial migration and
will overwrite the folders — only use it if you want to rebuild from scratch.

---

## Editing or removing content

- **Edit** an item by editing its `.md` file and refreshing the browser. No
  manifest change is needed for edits.
- **Remove** an item by deleting its `.md` file, then running
  `python generate_content.py --scan` to drop it from the manifest.

---

## Notes

- No dependencies and no build step — just Python 3 (only for the helper script
  and the local server) and a browser.
- Reordering: edit the `files` arrays in `manifest.json` directly to change the
  order cards appear within a section.
