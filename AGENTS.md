# AGENTS.md

# Purpose
This repo is Sphinx documentation for Smap M&E and Case Management Tools.
Agents should optimize for clear, consistent reStructuredText and low-noise builds.

# Sources Of Truth
- `CLAUDE.md` and `README.md` describe build setup and repo structure.
- `conf.py` controls Sphinx behavior and extensions.

# Build, Lint, Test
## Build HTML (standard)
```bash
make html
```

## Build And Package
```bash
./go.sh
```
Creates `docs.tgz` from `_build/html`.

## Clean Artifacts
```bash
make clean
```

## Single Page Build (best-effort)
No dedicated test runner exists. Use Sphinx directly for a focused build:
```bash
sphinx-build -b html -D master_doc=admin-api . _build/html
```
Notes:
- `master_doc` takes the docname without `.rst`.
- This still reads config from `conf.py`.
- If you need warnings as errors, add `-W`.

## Lint
No lint tooling is defined in this repo.

## Tests
No automated tests are defined.

# Dev Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install sphinx
pip install sphinx_rtd_theme
pip install sphinxcontrib-httpdomain
pip install sphinxcontrib-jquery
```

# Repo Layout
- Root contains most `.rst` pages.
- `index.rst` is the master toctree entry.
- Static assets live in `_static/` and images in `_images/`.
- `_build/` is generated output and should not be committed.

# Cursor / Copilot Rules
- No `.cursor/rules/`, `.cursorrules`, or `.github/copilot-instructions.md` found.

# Style Guidelines (Docs)
## reStructuredText Basics
- Use `.rst` for all content pages.
- Use section titles with underline adornments matching existing files:
  - Top-level: `=`
  - Section: `-`
  - Subsection: `+`
- Keep blank lines before and after directives.
- Indent directive content by two spaces.
- Prefer sentence case headings and consistent capitalization.

## Structure And Navigation
- Add new pages to the relevant `.. toctree::` in `index.rst` or a parent page.
- Use `.. contents::` with `:local:` for long pages when it matches existing pages.
- Keep the toctree ordered and grouped by topic.

## Cross-References
- Define labels above sections: `.. _label-name:`.
- Use `:ref:` for internal links.
- Use `:dfn:` for glossary-like term definitions.

## API Documentation (httpdomain)
- Use `.. http:get::`, `.. http:post::`, etc.
- Provide `:synopsis:` for each endpoint.
- Use `:query`, `:reqheader`, and `:statuscode` for parameters and responses.
- Include **Example request** and **Example response** blocks when possible.
- Prefer `.. sourcecode:: http` for request/response samples.

## Images And Figures
- Place images in `_images/`.
- Use `.. figure::` or `.. image::`.
- Always include `:alt:`.
- Add `:width:` and `:align:` when it improves layout.

## Tables
- Use `.. csv-table::` for simple data.
- Use `.. list-table::` for complex layouts.
- External CSVs can live in `tables/`.

## Formatting And Text
- Wrap long lines for readability, but preserve existing wrapping patterns.
- Use bold for UI labels and emphasis, not for entire paragraphs.
- Use literal blocks or `.. code-block::` for commands and code samples.
- Keep lists tight and parallel in structure.
- Avoid smart quotes; `smartquotes = False` in config.

## Naming Conventions (Files)
- Admin pages: `admin-*.rst`
- Server admin: `server-admin-*.rst`
- Analysis: `analysis-*.rst`
- XLS editor: `xls-*.rst`
- Online editor: `online-*.rst`
- API docs: `*-api.rst`
- Tips: `tips-*.rst`
- Reference: `ref-*.rst`

## Error Handling In Docs
- Document version-specific behavior with clear notes.
- Use `.. note::` for caveats and `.. warning::` for risky actions.
- For API errors, add `:statuscode` entries and describe error cases.

# Code Style (Non-Docs)
This repo is mostly docs. If you edit Python or shell files:
- Keep imports minimal; standard library first, then third-party.
- Use existing formatting style in `conf.py` (4-space indents).
- Avoid adding new dependencies unless required for Sphinx.
- Shell scripts should be POSIX compatible like `go.sh`.

# Build Hygiene
- Ensure `_build/html` exists before building: `mkdir -p _build/html`.
- Do not commit `_build/` output.

# Safe Defaults For Agents
- Prefer updating existing `.rst` content over adding new files.
- Verify cross-references and labels if you change headings.
- Keep API examples consistent with `httpdomain` format.
- When uncertain about placement, search for similar pages and mirror layout.

# Useful Commands Cheat Sheet
```bash
make html
make clean
./go.sh
sphinx-build -b html -D master_doc=admin-api . _build/html
```
