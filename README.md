# Terra MCP Server
A Model Context Protocol server that allows LLMs to configure the [TerraAPI dashboard](https://dashboard.tryterra.co/).

> [!NOTE]
> You will need your `TERRA_API_KEY` and `TERRA_DEV_ID` which is available from the [dashboard](https://dashboard.tryterra.co/)

## Installation

### Using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will
use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *terramcp*.

#### `uv` Installation
_Mac / Linux_
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
_Windows_
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Using PIP

Alternatively you can install `terramcp` via pip:

```bash
pip install terramcp
```

After installation, you can run it as a script using:

```bash
python -m terramcp
```

## Configuration

### Configure for Claude.app

Add to your Claude settings:

<details>
<summary>Using uvx</summary>

```json
{
  "mcpServers": {
    "terramcp": {
      "command": "uvx",
      "args": ["terramcp"],
      "env": {
        "TERRA_API_KEY": "your_api_key_here",
        "TERRA_DEV_ID": "your-dev-id-here",
      }
    }
  }
}
```
</details>

<details>
<summary>Using pip installation</summary>

```json
{
  "mcpServers": {
    "terramcp": {
      "command": "python",
      "args": ["-m", "terramcp"],
      "env": {
        "TERRA_API_KEY": "your_api_key_here",
        "TERRA_DEV_ID": "your-dev-id-here",
      }
    }
  }
}
```
</details>

### Configure for Zed

Add to your Zed settings.json:

<details>
<summary>Using uvx</summary>

```json
"context_servers": [
  "terramcp": {
    "command": "uvx",
    "args": ["terramcp"],
    "env": {
        "TERRA_API_KEY": "your_api_key_here",
        "TERRA_DEV_ID": "your-dev-id-here",
    }
  }
],
```
</details>

<details>
<summary>Using pip installation</summary>

```json
"context_servers": {
  "terramcp": {
    "command": "python",
    "args": ["-m", "terramcp"],
    "env": {
        "TERRA_API_KEY": "your_api_key_here",
        "TERRA_DEV_ID": "your-dev-id-here",
    }
  }
},
```
</details>

### Configure for VS Code

For quick installation, use one of the one-click install buttons below...

[![Install with UV in VS Code](https://img.shields.io/badge/VS_Code-UV-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=terramcp&config=%7B%22command%22:%22uvx%22,%22args%22:%5B%22terramcp%22%5D%7D) [![Install with UV in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-UV-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=terramcp&config=%7B%22command%22:%22uvx%22,%22args%22:%5B%22terramcp%22%5D%7D&quality=insiders)

For manual installation, add the following JSON block to your User Settings (JSON) file in VS Code. You can do this by pressing `Ctrl + Shift + P` and typing `Preferences: Open User Settings (JSON)`.

Optionally, you can add it to a file called `.vscode/mcp.json` in your workspace. This will allow you to share the configuration with others.

> Note that the `mcp` key is needed when using the `mcp.json` file.

<details>
<summary>Using uvx</summary>

```json
{
  "mcp": {
    "servers": {
      "terramcp": {
        "command": "uvx",
        "args": ["terramcp"],
        "env": {
            "TERRA_API_KEY": "your_api_key_here",
            "TERRA_DEV_ID": "your-dev-id-here",
        }
      }
    }
  }
}
```
</details>

## Debugging

You can use the MCP inspector to debug the server. For uvx installations:

```bash
npx @modelcontextprotocol/inspector uvx terramcp
```

Or if you've installed the package in a specific directory or are developing on it:

```bash
cd path/to/servers/src/terramcp
npx @modelcontextprotocol/inspector uv run terramcp
```

## License

terramcp is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the [LICENSE](https://github.com/tryterra/terramcp/blob/master/LICENSE) file in the project repository.