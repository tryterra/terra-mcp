from mcp.server.fastmcp import FastMCP
import requests
from typing import Optional

# Create an MCP server
mcp = FastMCP("Terra MCP Server", depencies=["requests"])

BASE_API_URL = "https://api.tryterra.co/v2"


# Get list of available integrations
@mcp.tool()
def terra_get_integrations() -> str:
    """
    Get list of available integrations.

    Returns:
        str: List of available integrations in json format
    """
    data = requests.get(f"{BASE_API_URL}/integrations")
    return data.json()


# Get detailed list of integrations
@mcp.tool()
def terra_get_detailed_integrations(
    sdk: Optional[bool] = None, dev_id: Optional[str] = None
) -> str:
    """
    Retrieve a detailed list of supported integrations, optionally filtered by the developer's enabled integrations and the requirement for SDK usage.

    Args:
        sdk (Optional[bool]): If true, allows SDK integrations to be included in the response.
        dev_id (Optional[str]): Developer ID to filter the integrations list based on the developer's enabled integrations.

    Returns:
        str: Detailed list of integrations in json format
    """
    params = {}
    if sdk is not None:
        params["sdk"] = sdk
    if dev_id is not None:
        params["dev_id"] = dev_id

    data = requests.get(f"{BASE_API_URL}/integrations/detailed", params=params)
    return data.json()


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}! Welcome to the Terra MCP server!"


if __name__ == "__main__":
    mcp.run(transport="stdio")
