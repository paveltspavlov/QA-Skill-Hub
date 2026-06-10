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
- **Filter** with the pills (All / Agents / Skills / Prompts) or **search** by name,
  summary, or tag.
- **Click a card** to expand it and read the full body.
- Inside an expanded card, toggle between:
  - **Markdown** — the full reference body.
  - **YAML** — the frontmatter you paste into a Copilot/Claude skill file.
- **Copy** copies whichever format is currently selected.

### Where the copied content goes

To install an item in your own project, copy it and save it as a Markdown file
inside your repo's `.copilot/skills/` folder (or wherever your AI tool reads
skills from), e.g. `.copilot/skills/commit-message-writer.md`.

---

## Adding new content

There are two ways to add an item.

### Option A — add a file by hand (recommended)

1. Create a new `.md` file in the appropriate folder (`Agents/`, `Skills/`, or
   `Prompts/`). Name it after its `id`, e.g. `Skills/my-new-skill.md`.
2. Give it frontmatter and a body (see the format above). Minimum fields:
   `id`, `name`, `folder` (`agents` | `skills` | `prompts`), and `summary`.
   `tags`, `aiTools`, and `istqbTopics` are optional lists.
3. Register it in the manifest by rescanning the folders:

   ```bash
   python generate_content.py --scan
   ```

   This rebuilds `manifest.json` from whatever `.md` files are present. Existing
   ordering is preserved, brand-new files are appended, and deleted files are
   dropped.
4. Refresh the browser — the new card appears in its section.

> **Why the `--scan` step?** The app is fully static, so the browser can't list a
> folder's contents on its own. `manifest.json` is the index it reads instead, and
> `--scan` keeps that index in sync with the files on disk.

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
