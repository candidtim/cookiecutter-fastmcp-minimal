from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

mcp = FastMCP("{{cookiecutter.package_name}} custom HTTP routes")

WELCOME = """
It works!

The development environment is now set up and you can start coding! Check out
the README.md for the development environment usage.

If you are new to FastMCP, see https://gofastmcp.com/getting-started/welcome
to get up and running quickly.
""".strip()


@mcp.custom_route("/", methods=["GET"])
async def index(request: Request) -> PlainTextResponse:
    return PlainTextResponse(WELCOME)


@mcp.custom_route("/health", methods=["GET"])
async def health(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")
