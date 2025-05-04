#!/usr/bin/env python3

import logging
import os
from typing import Optional, List
from mcp.server.fastmcp import Context

from src.api import twist_request

logger = logging.getLogger("twist-mcp-server")

def twist_inbox_get(
    ctx: Context,
    limit: Optional[int] = None,
    newer_than_ts: Optional[int] = None,
    older_than_ts: Optional[int] = None,
    archive_filter: Optional[str] = None,
    order_by: Optional[str] = None,
    exclude_thread_ids: Optional[List[int]] = None
) -> str:
    """Get the authenticated user's inbox.

    Args:
        limit: Limits the number of threads returned (default is 30, maximum is 500)
        newer_than_ts: Limits threads to those newer when the specified Unix time
        older_than_ts: Limits threads to those older when the specified Unix time
        archive_filter: Filter threads based on their is_archived flag: 'all', 'archived', or 'active' (default)
        order_by: Order of threads: 'desc' (default) or 'asc', based on last_updated attribute
        exclude_thread_ids: Thread IDs to exclude from results
    """
    # Get the token from the context
    token = ctx.request_context.lifespan_context.twist_token

    # Get the workspace ID from environment
    workspace_id = os.getenv("TWIST_WORKSPACE_ID")
    if not workspace_id:
        logger.error("TWIST_WORKSPACE_ID environment variable is required")
        return "Error: TWIST_WORKSPACE_ID environment variable is required"

    # Build parameters
    params = {"workspace_id": workspace_id}

    if limit is not None:
        params["limit"] = limit
    if newer_than_ts is not None:
        params["newer_than_ts"] = newer_than_ts
    if older_than_ts is not None:
        params["older_than_ts"] = older_than_ts
    if archive_filter is not None:
        params["archive_filter"] = archive_filter
    if order_by is not None:
        params["order_by"] = order_by
    if exclude_thread_ids is not None:
        params["exclude_thread_ids"] = exclude_thread_ids

    try:
        logger.info(f"Getting inbox for workspace ID: {workspace_id}")

        # Make the API request
        inbox_data = twist_request("inbox/get", params=params, token=token)

        if not inbox_data:
            logger.info("No inbox threads found")
            return "No inbox threads found"

        logger.info(f"Retrieved {len(inbox_data)} inbox threads")
        return inbox_data
    except Exception as error:
        logger.error(f"Error getting inbox: {error}")
        return f"Error getting inbox: {str(error)}"
