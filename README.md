# Twist MCP Server (testing)

An MCP server for interacting with a [Twist](https://twist.com/home) workspace. Written in Python using the [Twist REST API](https://developer.twist.com/v3/). Currently for testing purposes only.

## Installation

### Prerequisites

- Python 3.10+
- UV package manager ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))
- Twist API token
- Twist Workspace ID

### Getting a Twist API Token

1. Log in to your Twist account
2. Visit the [Twist App console](https://twist.com/app_console)
3. Create a new application for personal use
4. Copy the OAuth 2 test token; this token will give the MCP server full scope access to the currently logged in user.

Future versions will use proper OAuth authentication.

### Configuration with Claude Desktop

Add the Twist MCP server to the set of MCP servers in your claude_desktop_config.json:

```json
{
  "mcpServers": {
    "twist": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/twist-mcp-server",
        "run",
        "main.py"
      ],
      "env": {
        "TWIST_API_TOKEN": "your_twist_api_token",
        "TWIST_WORKSPACE_ID": "your_twist_workspace_id"
      }
    }
  }
}
```

## Available Tools

To see currently available tools, run:

```sh
# With GNU grep installed as ggrep (as with `brew install grep` on Mac)
ggrep -Po '(?<=^mcp.tool\(\)\()([^)]+)' main.py
```

As of now, the following tools are available:

- Inbox
  - `twist_inbox_get`: Get the contents of the user's inbox

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
