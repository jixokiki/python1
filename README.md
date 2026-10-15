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
