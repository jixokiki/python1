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
