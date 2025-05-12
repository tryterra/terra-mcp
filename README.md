# Terra MCP Server
MCP Server for V5 API

## Development

1. Install project dependencies using `uv`
```sh
uv sync
```

2. Run dev server
```
mcp dev server.py
```

## Deployment

1. In your Claude Desktop `claude_desktop_config.json` add this
```json
{
  "mcpServers": {
    "Terra MCP Server": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/terra-mcp",
        "run",
        "server.py"
      ],
      "env": {
        "TERRA_API_KEY": "your_api_key_here",
        "TERRA_DEV_ID": "your-dev-id-here",
      }
    }
  }
}
```

3. Open Claude Desktop