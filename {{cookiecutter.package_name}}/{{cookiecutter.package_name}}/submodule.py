from typing import Annotated

from fastmcp import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

mcp = FastMCP("{{cookiecutter.package_name}} submodule")


@mcp.tool(
    annotations=ToolAnnotations(
        readOnlyHint=True,
        openWorldHint=False,
        idempotentHint=True,
    )
)
async def add(
    a: Annotated[int, Field("Addend on the left")],
    b: Annotated[int, Field("Addend on the right")],
) -> int:
    """Add two numbers"""
    return a + b
