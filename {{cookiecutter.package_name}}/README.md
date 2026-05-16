# {{cookiecutter.application_name}}

{{cookiecutter.application_name}} description

## Quick Start

Install the dependencies and run the application:

    uv lock  # <- first time only, or after a change in declared dependencies
    uv sync
    uv run fastmcp run {{cookiecutter.package_name}}/__init__.py:create_server --transport http --reload

And then open it at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Point your [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) to http://127.0.0.1:8000/mcp , or run the inspector directly with `fastmcp` CLI:

    uv run fastmcp dev inspector {{cookiecutter.package_name}}/__init__.py:create_server --reload

See [FastMCP - Running](https://gofastmcp.com/cli/running) for more ways to run the server.

## Prerequisites

Python >=3.10

## Development environment

This project uses [uv](https://docs.astral.sh/uv/).

Quick start:

    uv lock  # creates or updates a lock file

    uv sync

    uv run pytest
    {%- if cookiecutter.use_ruff == 'y' %}
    uv run ruff format [--check]
    uv run ruff check [--fix] [--extend-select=I]{%- endif %}
    {%- if cookiecutter.use_mypy == 'y' %}
    uv run mypy{% endif %}

## Configuration

Configutaion is loaded from these sources in this order (the latter override the former):

 - default configuration is defined in `config.py`
 - `.env` file, if present (local file is ignored in Git)
 - environment variables (override the `.env` file)

See [Starlette - Configuration](https://starlette.dev/config/) for more information.
