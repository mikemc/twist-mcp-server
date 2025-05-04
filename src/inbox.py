#!/usr/bin/env python3

import logging
import os
from typing import Optional, List, Union
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
    token = ctx.request_context.lifespan_context.twist_token

    workspace_id = os.getenv("TWIST_WORKSPACE_ID")
    if not workspace_id:
        logger.error("TWIST_WORKSPACE_ID environment variable is required")
        return "Error: TWIST_WORKSPACE_ID environment variable is required"

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

        inbox_data = twist_request("inbox/get", params=params, token=token)

        if not inbox_data:
            logger.info("No inbox threads found")
            return "No inbox threads found"

        logger.info(f"Retrieved {len(inbox_data)} inbox threads")
        return inbox_data
    except Exception as error:
        logger.error(f"Error getting inbox: {error}")
        return f"Error getting inbox: {str(error)}"

def twist_inbox_archive_all(
    ctx: Context,
    older_than_ts: Optional[int] = None
) -> str:
    """Archives all threads in a workspace.

    Args:
        older_than_ts: Only archives threads that are the same or older than this timestamp
    """
    token = ctx.request_context.lifespan_context.twist_token

    workspace_id = os.getenv("TWIST_WORKSPACE_ID")
    if not workspace_id:
        logger.error("TWIST_WORKSPACE_ID environment variable is required")
        return "Error: TWIST_WORKSPACE_ID environment variable is required"

    params = {"workspace_id": workspace_id}

    if older_than_ts is not None:
        params["older_than_ts"] = older_than_ts

    try:
        logger.info(f"Archiving all inbox threads for workspace ID: {workspace_id}")

        result = twist_request("inbox/archive_all", params=params, token=token, method="POST")

        logger.info("Successfully archived all inbox threads")
        return "Successfully archived all inbox threads"
    except Exception as error:
        logger.error(f"Error archiving all inbox threads: {error}")
        return f"Error archiving all inbox threads: {str(error)}"

def twist_inbox_archive(
    ctx: Context,
    id: int
) -> str:
    """Archives a thread.

    Args:
        id: The ID of the thread to archive
    """
    token = ctx.request_context.lifespan_context.twist_token

    params = {"id": id}

    try:
        logger.info(f"Archiving thread with ID: {id}")

        result = twist_request("inbox/archive", params=params, token=token, method="POST")

        logger.info(f"Successfully archived thread with ID: {id}")
        return f"Successfully archived thread with ID: {id}"
    except Exception as error:
        logger.error(f"Error archiving thread: {error}")
        return f"Error archiving thread: {str(error)}"

def twist_inbox_unarchive(
    ctx: Context,
    id: int
) -> str:
    """Unarchives a thread.

    Args:
        id: The ID of the thread to unarchive
    """
    token = ctx.request_context.lifespan_context.twist_token

    params = {"id": id}

    try:
        logger.info(f"Unarchiving thread with ID: {id}")

        result = twist_request("inbox/unarchive", params=params, token=token, method="POST")

        logger.info(f"Successfully unarchived thread with ID: {id}")
        return f"Successfully unarchived thread with ID: {id}"
    except Exception as error:
        logger.error(f"Error unarchiving thread: {error}")
        return f"Error unarchiving thread: {str(error)}"

def twist_inbox_mark_all_read(
    ctx: Context
) -> str:
    """Marks all inbox threads in the workspace as read.
    """
    token = ctx.request_context.lifespan_context.twist_token

    workspace_id = os.getenv("TWIST_WORKSPACE_ID")
    if not workspace_id:
        logger.error("TWIST_WORKSPACE_ID environment variable is required")
        return "Error: TWIST_WORKSPACE_ID environment variable is required"

    params = {"workspace_id": workspace_id}

    try:
        logger.info(f"Marking all inbox threads as read for workspace ID: {workspace_id}")

        result = twist_request("inbox/mark_all_read", params=params, token=token, method="POST")

        logger.info("Successfully marked all inbox threads as read")
        return "Successfully marked all inbox threads as read"
    except Exception as error:
        logger.error(f"Error marking all inbox threads as read: {error}")
        return f"Error marking all inbox threads as read: {str(error)}"

def twist_inbox_get_count(
    ctx: Context
) -> Union[str, dict]:
    """Gets inbox count in a workspace for the authenticated user.
    """
    token = ctx.request_context.lifespan_context.twist_token

    workspace_id = os.getenv("TWIST_WORKSPACE_ID")
    if not workspace_id:
        logger.error("TWIST_WORKSPACE_ID environment variable is required")
        return "Error: TWIST_WORKSPACE_ID environment variable is required"

    params = {"workspace_id": workspace_id}

    try:
        logger.info(f"Getting inbox count for workspace ID: {workspace_id}")

        count_data = twist_request("inbox/get_count", params=params, token=token)

        if not count_data:
            logger.info("Failed to get inbox count")
            return "Failed to get inbox count"

        logger.info(f"Retrieved inbox count: {count_data}")
        return count_data
    except Exception as error:
        logger.error(f"Error getting inbox count: {error}")
        return f"Error getting inbox count: {str(error)}"
