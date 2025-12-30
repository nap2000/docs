# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains Sphinx-based documentation for Smap M&E and Case Management Tools. Smap provides digital tools for evaluation, monitoring, guidance, and case management applications.

## Build Commands

### Build HTML Documentation
```bash
make html
```
Output is generated in `_build/html/`

### Build and Package Documentation
```bash
./go.sh
```
This runs `make html` and creates a `docs.tgz` tarball containing the built documentation from `_build/html/`

### Clean Build Artifacts
```bash
make clean
```

## Development Environment Setup

1. Create a Python virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
```

2. Install required dependencies:
```bash
pip install sphinx
pip install sphinx_rtd_theme
pip install sphinxcontrib-httpdomain
pip install sphinxcontrib-jquery
```

3. Ensure the `_build/html` directory exists before building:
```bash
mkdir -p _build/html
```

## Documentation Structure

### Source Files
- **RST files in root directory**: Content files written in reStructuredText format (e.g., `admin-api.rst`, `getting-started.rst`)
- **index.rst**: Main documentation entry point with table of contents
- **conf.py**: Sphinx configuration (project metadata, theme settings, extensions)

### Static Resources
- **_images/**: Screenshots and diagrams used in documentation
- **_static/**: Custom CSS and static assets (theme overrides, favicon)
- **tables/**: Additional table data referenced by documentation

### Build Output
- **_build/**: Generated HTML output (not committed to git)

## Sphinx Configuration Details

### Theme
Uses `sphinx_rtd_theme` (Read the Docs theme) with custom CSS overrides in `_static/theme_overrides.css`

### Extensions
- `sphinx_rtd_theme`: Read the Docs theme
- `sphinxcontrib.jquery`: jQuery support for Sphinx
- `sphinxcontrib.httpdomain`: HTTP domain for documenting REST APIs

### Special Settings
- Primary domain is JavaScript (`primary_domain = 'js'`) for XPath function syntax compatibility
- Source files use `.rst` extension (reStructuredText)
- Master document is `index.rst`
- `smartquotes = False` to prevent smart quote conversion

## Content Organization

Documentation covers several major areas:
- **Getting Started**: Initial setup and account creation
- **Survey Design**: Form creation, question types, expressions
- **Administration**: User management, RBAC, server configuration
- **Analysis**: Dashboards, data export, external integrations
- **Case Management**: Task workflows, console, notifications
- **APIs**: Server APIs, data access, webhooks
- **FieldTask**: Android app for data collection
- **WebForms**: Web-based form completion

## File Naming Conventions

- Admin pages: `admin-*.rst`
- Server administration: `server-admin-*.rst`
- Analysis features: `analysis-*.rst`
- XLS form editor topics: `xls-*.rst`
- Online editor topics: `online-*.rst`
- API documentation: `*-api.rst`
- Tips and troubleshooting: `tips-*.rst`
- Reference material: `ref-*.rst`

## Key Architectural Notes

### API Documentation Format
API endpoints are documented using the `httpdomain` extension, which provides specialized directives for HTTP methods, routes, and parameters.

### Cross-References
The documentation uses Sphinx's cross-referencing system extensively:
- `:ref:\`label\`` for internal references
- `:dfn:\`term\`` for definitions in the glossary
- Labels are defined with `.. _label-name:` above sections

### Content Inclusion Pattern
Many pages use `.. contents:: :local:` to generate page-level table of contents.

## Common Tasks

### Adding a New Documentation Page
1. Create new `.rst` file in repository root
2. Add appropriate content using reStructuredText syntax
3. Add the file to the toctree in `index.rst` or relevant parent page
4. Run `make html` to verify the page builds correctly

### Updating Images
1. Place new images in `_images/` directory
2. Reference them using `.. figure::` or `.. image::` directives
3. Always include `:alt:` text for accessibility

### Working with Tables
Use either:
- `.. csv-table::` for simple tabular data
- `.. list-table::` for more complex tables
- External CSV files from `tables/` directory can be included

### Testing Local Changes
1. Run `make html` to build
2. Open `_build/html/index.html` in a browser to review changes
3. Check for warnings/errors in build output

## Deployment
Built documentation is deployed by copying the contents of `_build/html/` to a web server directory accessible via HTTP.
