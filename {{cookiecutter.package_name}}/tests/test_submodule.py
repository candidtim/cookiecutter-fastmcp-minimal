from fastmcp import Client

from {{cookiecutter.package_name}}.submodule import mcp


async def test_add():
    async with Client(mcp) as client:
        result = await client.call_tool("add", {"a": 2, "b": 3})
        assert result.structured_content == {"result": 5}
