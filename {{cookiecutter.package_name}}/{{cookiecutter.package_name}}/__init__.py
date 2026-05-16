from fastmcp import FastMCP

from .custom_routes import mcp as custom_routes_mcp
from .logging import init_logging
from .submodule import mcp as submodule_mcp

INSTRUCTIONS = """
Describe the MCP server here and provide initial instructions to the agents about how
to use it: what it's for, when to use it, where to start (entry points tools), etc.
""".strip()


def create_server() -> FastMCP:
    init_logging()

    mcp = FastMCP("{{cookiecutter.package_name}}", instructions=INSTRUCTIONS)
    mcp.mount(submodule_mcp)
    mcp.mount(custom_routes_mcp)

    return mcp
