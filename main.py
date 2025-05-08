#!/usr/bin/env python3

import logging
import inspect
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from dataclasses import dataclass

from mcp.server.fastmcp import FastMCP

from src.api import get_api_client
import src.inbox
import src.threads

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("twist-mcp-server")

# Create lifespan context type for type hints
@dataclass
class TwistContext:
    twist_token: str

# Set up lifespan context manager
@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[TwistContext]:
    """Manage application lifecycle with type-safe context"""
    # Initialize Twist token on startup
    try:
        twist_token = get_api_client()
        yield TwistContext(twist_token=twist_token)
    finally:
        # Any cleanup needed
        logger.info("Shutting down Twist MCP Server")

# Create an MCP server
mcp = FastMCP("Twist MCP Server", lifespan=app_lifespan)

# Register all tools from tool modules
for module in [src.inbox, src.threads]:
    for name, func in inspect.getmembers(module, inspect.isfunction):
        if name.startswith('twist_') and func.__module__ == module.__name__:
            logger.info(f"Registering tool: {name}")
            mcp.tool()(func)

# Run the server
if __name__ == "__main__":
    logger.info("Starting Twist MCP Server")
    # Run with stdio transport
    mcp.run(transport='stdio')
