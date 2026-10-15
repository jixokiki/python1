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
