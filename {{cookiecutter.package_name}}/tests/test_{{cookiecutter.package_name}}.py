from fastmcp import Client
from starlette.testclient import TestClient

from {{cookiecutter.package_name}} import create_server


async def test_wriring(client: Client):
    tools = await client.list_tools()
    assert len(tools) == 1
    assert tools[0].name == "add"


def test_health():
    mcp = create_server()
    client = TestClient(mcp.http_app())
    response = client.get("/health")
    assert response.status_code == 200
    assert response.text == "OK"
