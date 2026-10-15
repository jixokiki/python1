#!/usr/bin/env bash
set -euo pipefail

mkdir -p \
  docs \
  .github/workflows \
  .github/ISSUE_TEMPLATE

echo "Membuat dokumentasi repository..."

cat > README.md <<'EOF'
# Python Learning & Projects

A collection of Python learning exercises, programming fundamentals,
web application experiments, database integrations, and small projects.

## Overview

This repository preserves a collection of Python experiments and
projects developed while learning and implementing Python concepts.

### Repository contents

| Path | Description |
| --- | --- |
| `ClassObject.py` | Object-oriented programming example |
| `PythonArrayImplementation.py` | Array implementation exercise |
| `PythonKeywordsAndIdentifier.py` | Keywords and identifiers exercise |
| `PythonMockTest1/`–`PythonMockTest4/` | Practice exercises and mock tests |
| `Project/` | Additional learning projects |
| `form-to-mysql/` | Form and MySQL integration project |
| `product-purchase/` | Product purchase application experiment |
| `templates/`, `templates2/` | HTML templates used by web examples |
| `app.py`–`app7.py` | Python application experiments |
| `web.py`, `webadmin*.py` | Web application and admin experiments |
| `database_management*.py` | Database management examples |

> This is a multi-project learning repository. Individual folders may
> have different dependencies, entry points, and configuration requirements.

## Technology

- Python
- Flask and web application fundamentals
- SQLite
- MySQL integration
- HTML templates
- Git and GitHub

Technologies listed above reflect the repository's apparent scope.
Check each project's source code and dependencies before running it.

## Getting started

### 1. Requirements

- Python 3.10 or newer recommended
- Git
- MySQL only for projects that require a MySQL server

Some legacy projects may require older dependency versions.

### 2. Clone the repository

```bash
git clone git@github.com:jixokiki/python1.git
cd python1
```

### 3. Create a virtual environment

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Some projects may need additional dependencies or database configuration.
See `INSTALL-INSTRUCTIONS.md`.

### 5. Run a project

For example, if `app.py` is a Flask application:

```bash
python app.py
```

Review the selected file before running it. Different projects can have
different entry points and configuration requirements.

## Configuration and security

- Never commit passwords, API keys, tokens, or production credentials.
- Use environment variables for sensitive configuration.
- Database files may contain data; inspect them before publishing.
- Do not assume every application is production-ready.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [API reference](docs/API.md)
- [Development guide](docs/DEVELOPMENT.md)
- [Deployment guide](docs/DEPLOYMENT.md)
- [Quality checks](docs/QUALITY-CHECKS.md)
- [Installation instructions](INSTALL-INSTRUCTIONS.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Changelog](CHANGELOG.md)

## Development status

This repository contains learning exercises and legacy experiments.
Setup and deployment instructions should be verified for each project
before use in a new environment.

## License

No license has been specified yet. All rights remain with their
respective copyright holders until a license is explicitly added.
EOF

cat > .gitignore <<'EOF'
# Python bytecode
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
.venv/
venv/
env/
ENV/

# Environment variables and secrets
.env
.env.*
!.env.example
*.pem
*.key

# Tool caches
.pytest_cache/
.mypy_cache/
.ruff_cache/
.coverage
htmlcov/

# IDE and operating system
.DS_Store
.idea/
.vscode/
*.swp
*.swo

# Build artifacts
build/
dist/
*.egg-info/

# Logs
*.log
EOF

cat > .editorconfig <<'EOF'
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
indent_style = space
indent_size = 4

[*.{yml,yaml,json}]
indent_size = 2

[*.md]
trim_trailing_whitespace = false
EOF

cat > INSTALL-INSTRUCTIONS.md <<'EOF'
# Installation Instructions

## Prerequisites

- Git
- Python 3.10 or newer recommended
- MySQL server for projects that use MySQL

## Clone

```bash
git clone git@github.com:jixokiki/python1.git
cd python1
```

## Create an isolated environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

On Windows, activate with `.venv\Scripts\Activate.ps1`.

## Install dependencies

```bash
pip install -r requirements.txt
```

Some historical projects may require dependencies not listed in the
root requirements file. Inspect the relevant source code first.

## Run

Choose a specific project or script and inspect its entry point.
For a Flask application, the command may be:

```bash
python app.py
```

Do not assume all scripts can run simultaneously or use the same database.

## Database setup

SQLite projects may use local `.db` files. MySQL projects may require
a running MySQL server and project-specific connection settings.
Never put database passwords in source control.
EOF

cat > docs/ARCHITECTURE.md <<'EOF'
# Architecture

## Repository model

This repository is a collection of Python exercises and small applications,
not a single unified application.

## Main areas

- Standalone Python scripts: language fundamentals and practice.
- Mock test folders: grouped learning exercises.
- Web experiments: scripts such as `app.py`, `web.py`, and `webadmin*.py`.
- Templates: HTML files used by selected web experiments.
- Database examples: SQLite files and database management scripts.
- Separate projects: `Project/`, `form-to-mysql/`, and `product-purchase/`.

## Runtime boundaries

Each project may have its own entry point, dependency requirements,
database schema, and configuration. Confirm these from the source code.

## Data flow

A typical web project may follow this flow:

1. Browser submits a request.
2. Python web application processes the request.
3. Application code reads or writes to its configured database.
4. A response or rendered HTML template is returned.

This is a general model; verify the actual flow in each project.

## Future improvements

- Separate independent applications into clearly named directories.
- Add project-specific README files.
- Add automated tests and reproducible dependency versions.
- Move credentials into environment variables.
EOF

cat > docs/API.md <<'EOF'
# API Reference

## Scope

The repository contains multiple experiments. A complete API specification
cannot be inferred from filenames alone.

## How to document an endpoint

For each web application, document:

- HTTP method and route
- Purpose and expected behavior
- Required parameters and request body
- Successful response and status code
- Validation and error responses
- Authentication requirements, if any

## How to inspect routes

Search the relevant Python files for Flask route decorators such as
`@app.route` and `@app.get`, or inspect the routing framework in use.

Do not treat this document as a claim that every project exposes an API.
Update it when actual routes have been verified.
EOF

cat > docs/DEVELOPMENT.md <<'EOF'
# Development Guide

## Setup

Follow `INSTALL-INSTRUCTIONS.md` and use an isolated virtual environment.

## Working on a project

1. Identify the target project and its entry point.
2. Read its imports and configuration.
3. Identify the database and required environment variables.
4. Install required dependencies.
5. Run the project locally.
6. Test changes before committing.

## Git workflow

```bash
git status
git switch -c feature/describe-your-change
git add <specific-files>
git commit -m "feat: describe your change"
```

Push the branch and open a pull request when using a collaboration workflow.

## Coding conventions

- Follow PEP 8 where practical.
- Use descriptive names.
- Keep secrets outside source control.
- Avoid unrelated changes in the same commit.
- Document project-specific setup and dependencies.

## Dependencies

Update `requirements.txt` only after verifying which dependencies
are required by the projects being maintained.
EOF

cat > docs/DEPLOYMENT.md <<'EOF'
# Deployment Guide

## Important

This repository contains multiple experiments. There is no single
deployment procedure that can be safely assumed for every project.

## Before deploying

- Select one application and identify its entry point.
- Verify its runtime and dependency versions.
- Configure environment variables and secrets.
- Configure the database and migrations, if applicable.
- Disable debug mode in production.
- Test the application locally.
- Review authentication, authorization, and error handling.

## Web application checklist

For a Flask-based application, use a production-capable WSGI server
appropriate to the deployment platform instead of relying on Flask's
development server for production traffic.

Configure logging, HTTPS, database access, backups, and monitoring
according to the target environment.

## Rollback

Keep a known-good revision and a database backup where applicable.
Verify the rollback procedure before a production release.
EOF

cat > docs/QUALITY-CHECKS.md <<'EOF'
# Quality Checks

## Baseline checks

Run these from the repository root:

```bash
python --version
python -m compileall -q .
git diff --check
git status --short
```

Compilation checks syntax; it does not prove that the applications work.

## Application checks

For each project:

- Install its dependencies.
- Run the application using its documented entry point.
- Verify expected routes and database behavior.
- Check validation and error handling.
- Run automated tests when available.

## Before publishing

- Check for credentials and private data.
- Review database files before committing.
- Confirm README commands match the actual project.
- Review the final diff before pushing.
EOF

cat > CONTRIBUTING.md <<'EOF'
# Contributing

Thank you for helping improve this repository.

## Guidelines

- Keep changes focused and explain their purpose.
- Preserve existing exercises unless a change is intentional.
- Include setup instructions for new projects.
- Add tests when practical.
- Never commit secrets or private data.

## Suggested workflow

1. Create a branch.
2. Make and test your changes.
3. Review `git diff` and `git status`.
4. Commit with a clear message.
5. Open a pull request describing the change and its tests.

## Commit message examples

- `docs: improve installation instructions`
- `fix: correct database connection handling`
- `feat: add input validation example`
- `test: add unit tests for utility functions`
EOF

cat > SECURITY.md <<'EOF'
# Security Policy

## Scope

This repository contains learning exercises and legacy project experiments.
Not every component is intended for production use.

## Reporting a vulnerability

Please do not publish passwords, tokens, personal data, or exploit details
in a public issue. Contact the repository owner privately through an
appropriate GitHub contact method.

## Security recommendations

- Never commit credentials or production environment files.
- Use least-privilege database accounts.
- Validate user input and use parameterized SQL queries.
- Disable debug mode in production.
- Review local database files for private or personal information.
- Rotate any credential that has been exposed.
EOF

cat > CHANGELOG.md <<'EOF'
# Changelog

Notable repository changes are documented here.

## Unreleased

- Add structured repository documentation.
- Add development, installation, security, and contribution guidance.
- Add GitHub Actions workflow and issue/PR templates.
- Add repository editor configuration and dependency update configuration.

Older changes have not yet been reconstructed from Git history.
EOF

cat > .github/workflows/ci.yml <<'EOF'
name: Python CI

on:
  push:
    branches: [master, main]
  pull_request:
    branches: [master, main]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  syntax-check:
    name: Python syntax check
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Check Python syntax
        run: python -m compileall -q .

      - name: Check whitespace errors
        run: git diff --check
EOF

cat > .github/dependabot.yml <<'EOF'
version: 2
updates:
  - package-ecosystem: pip
    directory: /
    schedule:
      interval: monthly
    open-pull-requests-limit: 5

  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: monthly
    open-pull-requests-limit: 5
EOF

cat > .github/ISSUE_TEMPLATE/bug_report.yml <<'EOF'
name: Bug report
description: Report a reproducible problem
title: "[Bug]: "
labels: ["bug"]
body:
  - type: textarea
    id: summary
    attributes:
      label: Problem
      description: Describe what happened.
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: Steps to reproduce
      placeholder: "1. Run...\n2. Enter...\n3. Observe..."
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Expected behavior
    validations:
      required: true
  - type: input
    id: python-version
    attributes:
      label: Python version
      placeholder: "e.g. Python 3.11"
  - type: textarea
    id: logs
    attributes:
      label: Error messages or logs
      description: Remove secrets and personal data before posting.
EOF

cat > .github/ISSUE_TEMPLATE/feature_request.yml <<'EOF'
name: Feature request
description: Suggest an improvement
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Problem or motivation
      description: What would this improvement solve?
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Proposed solution
    validations:
      required: true
  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives considered
EOF

cat > .github/PULL_REQUEST_TEMPLATE.md <<'EOF'
## Summary

Describe the changes and their purpose.

## Type of change

- [ ] Bug fix
- [ ] New feature or example
- [ ] Documentation
- [ ] Refactoring

## Validation

- [ ] I reviewed the changed files.
- [ ] I ran relevant checks.
- [ ] I removed secrets and private data.
- [ ] I updated documentation where needed.

## Notes

Add screenshots, test results, or follow-up work if applicable.
EOF

echo "Selesai membuat file dokumentasi dan konfigurasi."
