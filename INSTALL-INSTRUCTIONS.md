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
