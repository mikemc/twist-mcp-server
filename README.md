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

As of now, the following tools are available:

- Inbox
  - `twist_inbox_get`: Get the contents of the user's inbox
  - `twist_inbox_archive_all`: Archives all threads in a workspace (or, all threads after a given timestamp)
  - `twist_inbox_archive`: Archives a specific thread by ID
  - `twist_inbox_unarchive`: Unarchives a specific thread by ID
  - `twist_inbox_mark_all_read`: Marks all inbox threads as read
  - `twist_inbox_get_count`: Gets the count of inbox threads
- Threads
  - `twist_threads_getone`: Get a thread by ID
  - `twist_threads_get`: Get all threads in a channel
  - `twist_threads_add`: Add a new thread to a channel
  - `twist_threads_update`: Update an existing thread
  - `twist_threads_remove`: Remove a thread
  - `twist_threads_star`: Star a thread
  - `twist_threads_unstar`: Unstar a thread
  - `twist_threads_pin`: Pin a thread
  - `twist_threads_unpin`: Unpin a thread
  - `twist_threads_move_to_channel`: Move a thread to a different channel
  - `twist_threads_get_unread`: Get unread threads in the workspace
  - `twist_threads_mark_read`: Mark a thread as read
  - `twist_threads_mark_unread`: Mark a thread as unread
  - `twist_threads_mark_unread_for_others`: Mark a thread as unread for others
  - `twist_threads_mark_all_read`: Mark all threads as read in a workspace or channel
  - `twist_threads_clear_unread`: Clear unread threads in the workspace
  - `twist_threads_mute`: Mute a thread for a number of minutes
  - `twist_threads_unmute`: Unmute a thread

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
