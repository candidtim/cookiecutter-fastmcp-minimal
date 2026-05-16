import pytest
from fastmcp import Client

from {{cookiecutter.package_name}} import create_server


@pytest.fixture
async def client():
    mcp = create_server()
    async with Client(mcp) as client:
        yield client
