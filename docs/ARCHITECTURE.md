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
