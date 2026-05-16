# cookiecutter-fastmcp-minimal

From the author of [cookiecutter-flask-minimal](https://github.com/candidtim/cookiecutter-flask-minimal)! *A minimalist template for a minimalist MCP framework.*

This is a **minimalist's** **production-ready** [FastMCP](https://github.com/prefecthq/fastmcp) project template:

 - zero bloat
 - no dependencies except for [FastMCP](https://github.com/prefecthq/fastmcp) and [pytest](https://pytest.org)
 - complete project set-up as per FastMCP documentation and industry practices,
   including things like logging, configuration, testing and packaging
 - development environment with [uv](https://docs.astral.sh/uv/) and [ruff](https://astral.sh/ruff)
 - optional [mypy](https://www.mypy-lang.org) (or bring you favorite type checker, or none at all)

**Up to date with FastMCP 3 !**

## Usage

Install [cookiecutter](https://github.com/audreyr/cookiecutter):

    pip install --user cookiecutter

Create your application from this template:

    cookiecutter https://github.com/candidtim/cookiecutter-fastmcp-minimal.git

All set! Run the application:

    cd mymcp
    uv lock
    uv sync
    uv run fastmcp run mymcp/__init__.py:create_server --transport http --reload

And then open it at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Point your [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector)
to `http://127.0.0.1:8000/mcp`.

## Features

Included:

 - minimal production-ready FastMCP application with
   [server composition](https://gofastmcp.com/servers/composition#composing-servers)
   for modular development and simpler testing (no import-time wiring)

 - minimalist configuration system, based on the underlying
   [Starlette configuration](https://starlette.dev/config/)

 - basic logging configuration

 - sample test and testing set-up, as per
   [FastMCP test client](https://gofastmcp.com/clients/client)

 - `uv`-based development environment configuration, including a way
   to package and release the application

 - optional, yet **highly** recommended, configuration for `ruff` and `mypy`

 - well-documented development environment (see the generated `README.md`)

 - an initial `CLAUDE.md` to ramp up the coding agents, keep it up to date as
   you progress

Not included:

 - everything else: there is no vector database, SQLAlchemy, MongoKit, or
   anything else; it is up to you to chose how to implement your application

 - there are no sample features or examples of how to use FastMCP; this
   template is not intended as a tutorial, but as a well-configured starting
   point for a new implementation; refer to the
   [FastMCP documentation](https://gofastmcp.com/getting-started/welcome)
   to learn FastMCP if necessary

 - no choice on how to deploy the application is made, no ASGI container is
   chosen; see
   [HTTP Deployment](https://gofastmcp.com/deployment/http)
   for the options most suitable for your infrastructure

# Contributions

... are welcome! Feel free to create a pull request to fix bugs or keep up to date.

If you think some additional feature is indispensable, feel free to create an
issue or a pull request, but bare in mind that the goal of this template is to
stay a "minimal" one. If you would like to add a feature, maybe best way to do
so is to make it optional and off by default then. One can use cookiecutter's
choice variables, and, ultimately, hooks, in order to create an optional
feature.

If you do a change, use `make test` from root directory to test the updated template.

# Attributions

Configuration of this entire project template is based on
[FastMCP documentation](https://gofastmcp.com/getting-started/welcome) and is heavily
inspired by [Flask](https://flask.palletsprojects.com/en/3.0.x/) and
[Starlette](https://starlette.dev/) documentation. Please, note however, that
this template is not endoprsed by any of the above and is not guaranteed to follow
their recommndations precisely.
