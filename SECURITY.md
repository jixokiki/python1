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
