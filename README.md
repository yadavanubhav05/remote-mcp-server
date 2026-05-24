# remote-mcp-server

# Simple Calculator MCP Server

A minimal FastMCP server that exposes basic math tools and one JSON resource over `streamable-http`.

## Features

- `add(a, b)` -> returns the sum of two integers
- `subtract(a, b)` -> returns `a - b`
- `multiply(a, b)` -> returns `a * b`
- `random_number(min_val=1, max_val=100)` -> returns a random integer in range
- `info://server` resource -> server metadata in JSON

Implementation: [main.py](main.py)

## Requirements

- Python `>=3.14`
- Dependency: `fastmcp>=3.3.1`

Project metadata: [pyproject.toml](pyproject.toml)

## Setup

Using `uv` (recommended):

```bash
uv sync
```

## Run The Server

```bash
uv run python main.py
```

The server starts with:

- transport: `streamable-http`
- host: `0.0.0.0`
- port: `8000`

## Development (Inspector)

If you want to inspect tools/resources during development:

```bash
uv run fastmcp dev inspector main.py
```

## Available API Surface

### Tools

1. `add(a: int, b: int) -> int`
2. `random_number(min_val: int = 1, max_val: int = 100) -> int`
3. `multiply(a: int, b: int) -> int`
4. `subtract(a: int, b: int) -> int`

### Resource

- `info://server` (`application/json`)

## Notes

- This project is intentionally small and easy to extend.
- Add more tools in [main.py](main.py) using the `@mcp.tool()` decorator.
