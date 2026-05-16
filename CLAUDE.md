# CLAUDE.md

This file provides guidance to coding agents (Claude Code, OpenCode, Codex, etc.) when working with code in this repository.

## Commands

```bash
uv sync                        # install dependencies
uv run pytest                  # run all tests
uv run pytest tests/test_submodule.py::test_add  # run a single test
uv run ruff format             # format code
uv run ruff format --check     # check formatting without modifying
uv run ruff check --fix --extend-select=I  # lint and fix (including import sort)
uv run mypy                    # type check

# Run the MCP server (HTTP, with hot reload):
uv run fastmcp run {{cookiecutter.package_name}}/__init__.py:create_server --transport http --reload
```

## Architecture

This is a [FastMCP](https://gofastmcp.com) server. The entrypoint is `create_server()` in `{{cookiecutter.package_name}}/__init__.py`, which assembles a root `FastMCP` instance by mounting sub-MCPs.

**Composition pattern:** each logical area of functionality lives in its own module as a `FastMCP` instance (e.g. `submodule.py`, `custom_routes.py`). These are imported and mounted onto the root server in `__init__.py`. To add a new area of functionality, create a new module with its own `mcp = FastMCP(...)`, define tools/routes on it, and mount it in `create_server()`. Each module can be tested separately and does not require wiring the entire application to test it.

**Key files:**
- `{{cookiecutter.package_name}}/__init__.py` — assembles the server
- `{{cookiecutter.package_name}}/submodule.py` — example MCP tool (`add`); add new tools here or in a new mounted module
- `{{cookiecutter.package_name}}/custom_routes.py` — custom HTTP routes (index, `/health`)
- `{{cookiecutter.package_name}}/config.py` — all configuration via `starlette.config`; sources: defaults → `.env` → env vars
- `{{cookiecutter.package_name}}/logging.py` — logging setup; log level is `DEBUG` when `DEBUG=true`, else `INFO`

**Testing:** tests use `fastmcp.Client` for in-process MCP protocol calls and Starlette's `TestClient` for HTTP routes. The shared `client` fixture in `conftest.py` creates a `Client` wrapping the full assembled server.

## Configuration

Copy `.env.example` to `.env` for local overrides. The `.env` file is gitignored. See `{{cookiecutter.package_name}}/config.py` for all available configuration keys.
