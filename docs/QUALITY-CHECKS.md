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
