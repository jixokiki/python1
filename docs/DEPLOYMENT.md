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
