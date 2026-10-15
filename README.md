# Python Learning & Projects

A collection of Python learning exercises, desktop applications, web application experiments, and database integration projects.

## Overview

This repository contains Python exercises and application prototypes developed for learning, experimentation, and future reference.

It brings together programming fundamentals, GUI applications, Flask-based web applications, database examples, and mock test documentation.

> This is a multi-project repository. Each application may have different dependencies, entry points, database requirements, and setup procedures.

## Repository Structure

| Path | Description |
|---|---|
| `ClassObject.py` | Object-oriented programming exercise |
| `PythonArrayImplementation.py` | Array implementation exercise |
| `PythonKeywordsAndIdentifier.py` | Keywords and identifiers exercise |
| `Project/` | Standalone Python utilities and GUI applications |
| `PythonMockTest1/`–`PythonMockTest4/` | Mock test screenshots and practice references |
| `app.py`–`app7.py` | Web application experiments |
| `web.py`, `webadmin*.py` | Web and admin application experiments |
| `database_management*.py` | Database management examples |
| `form-to-mysql/` | Form and MySQL integration project |
| `product-purchase/` | Product purchase application experiment |
| `templates/`, `templates2/` | HTML templates |
| `docs/` | Architecture, API, deployment, development, and quality documentation |

## Technology

- Python
- Flask and Flask extensions
- SQLite
- MySQL Connector/Python
- Tkinter for desktop interfaces
- Pygame for game development
- HTML templates
- Git and GitHub

Dependencies vary by application. Refer to `requirements.txt` and the selected project's source code before installing or running it.

## Getting Started

### Prerequisites

- Git
- Python compatible with the selected application's dependencies
- MySQL Server for applications that require MySQL
- A graphical desktop environment for GUI applications

Python 3.10 or newer is a recommended starting point, but some legacy dependencies may require compatibility adjustments.

### 1. Clone the Repository

Using HTTPS:

```bash
git clone https://github.com/jixokiki/python1.git
cd python1
```

Alternatively, use SSH:

```bash
git clone git@github.com:jixokiki/python1.git
cd python1
```

### 2. Create a Virtual Environment

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On Windows, install additional platform-specific dependencies only if needed:

```powershell
python -m pip install -r requirements-windows.txt
```

Some older applications may need extra dependencies, operating-system libraries, or database configuration. See `INSTALL-INSTRUCTIONS.md` before running them.

### 4. Run an Application

Run a standalone script, for example:

```bash
python Project/AgeCalculator.py
```

A Flask application may use a command such as:

```bash
python app.py
```

These are examples, not universal entry points. Review the selected script and its configuration first. GUI applications require a graphical environment.

## Database Configuration

This repository includes examples that use SQLite and MySQL.

- Local database files are excluded from Git.
- Cloning the repository does not restore local database files.
- MySQL applications may require a running server, a database, and local credentials.
- Review the selected application's code to determine its expected tables and schema.
- Never commit database passwords, tokens, or private production data.

## Development Checks

Check Python syntax:

```bash
python -m compileall -q .
```

Check Git whitespace errors:

```bash
git diff --check
```

The repository also includes a GitHub Actions workflow for automated syntax checks.

## Documentation

- [Installation Instructions](INSTALL-INSTRUCTIONS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [API Reference](docs/API.md)
- [Development Guide](docs/DEVELOPMENT.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Quality Checks](docs/QUALITY-CHECKS.md)
- [Contributing](CONTRIBUTING.md)
- [Security Policy](SECURITY.md)
- [Changelog](CHANGELOG.md)

## Project Status

This repository contains educational exercises, prototypes, and legacy experiments. Applications should be tested independently before being used in a new environment or deployed publicly.

## License

No license has been specified. Do not assume that the code may be redistributed or reused without permission.
