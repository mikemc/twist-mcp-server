#!/usr/bin/env python3

import logging
import os
from typing import Optional, List, Union, Dict, Any
from mcp.server.fastmcp import Context

from src.api import twist_request

logger = logging.getLogger("twist-mcp-server")

def twist_threads_getone(
    ctx: Context,
    id: int
) -> Union[str, Dict[str, Any]]:
    """Gets a thread object by id.

    Args:
        id: The id of the thread
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Getting thread with ID: {id}")
        thread_data = twist_request("threads/getone", params=params, token=token)
        logger.info(f"Retrieved thread with ID: {id}")
        return thread_data
    except Exception as error:
        logger.error(f"Error getting thread: {error}")
        return f"Error getting thread: {str(error)}"

def twist_threads_get(
    ctx: Context,
    channel_id: int,
    as_ids: Optional[bool] = None,
    filter_by: Optional[str] = None,
    limit: Optional[int] = None,
    newer_than_ts: Optional[int] = None,
    older_than_ts: Optional[int] = None,
    before_id: Optional[int] = None,
    after_id: Optional[int] = None,
    workspace_id: Optional[int] = None,
    is_pinned: Optional[bool] = None,
    is_starred: Optional[bool] = None,
    order_by: Optional[str] = None,
    exclude_thread_ids: Optional[List[int]] = None
) -> Union[str, List[Dict[str, Any]]]:
    """Gets all threads in a channel.

    Args:
        channel_id: The id of the channel
        as_ids: If enabled, only the ids of the threads are returned
        filter_by: A filter can be one of "attached_to_me" or "everyone". Default is "everyone"
        limit: Limits the number of threads returned (default is 20, maximum is 500)
        newer_than_ts: Limits threads to those newer when the specified Unix time
        older_than_ts: Limits threads to those older when the specified Unix time
        before_id: Limits threads to those with a lower than the specified id
        after_id: Limits threads to those with a higher than the specified id
        workspace_id: The id of the workspace
        is_pinned: If enabled, only pinned threads are returned
        is_starred: If enabled, only starred threads are returned
        order_by: The order of the threads returned. Either "desc" (default) or "asc"
        exclude_thread_ids: The thread ids that should be excluded from the results
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Getting threads for channel ID: {channel_id}")
        threads_data = twist_request("threads/get", params=params, token=token)

        if not threads_data:
            logger.info("No threads found")
            return "No threads found"

        logger.info(f"Retrieved {len(threads_data)} threads")
        return threads_data
    except Exception as error:
        logger.error(f"Error getting threads: {error}")
        return f"Error getting threads: {str(error)}"

def twist_threads_add(
    ctx: Context,
    channel_id: int,
    title: str,
    content: str,
    actions: Optional[List[Dict[str, Any]]] = None,
    attachments: Optional[List[Dict[str, Any]]] = None,
    direct_group_mentions: Optional[List[int]] = None,
    direct_mentions: Optional[List[int]] = None,
    groups: Optional[List[int]] = None,
    recipients: Optional[Union[List[int], str]] = None,
    send_as_integration: Optional[bool] = None,
    temp_id: Optional[int] = None
) -> Union[str, Dict[str, Any]]:
    """Adds a new thread to a channel.

    Args:
        channel_id: The id of the channel
        title: The title of the new thread
        content: The content of the new thread
        actions: List of action buttons to the new thread
        attachments: List of attachments to the new thread
        direct_group_mentions: The groups that are directly mentioned
        direct_mentions: The users that are directly mentioned
        groups: The groups that will be notified
        recipients: An array of users that will be attached to the thread or "EVERYONE"
        send_as_integration: Displays the integration as the thread creator
        temp_id: The temporary id of the thread
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Adding thread to channel ID: {channel_id}")
        thread_data = twist_request("threads/add", params=params, token=token, method="POST")
        logger.info(f"Added thread with ID: {thread_data.get('id')}")
        return thread_data
    except Exception as error:
        logger.error(f"Error adding thread: {error}")
        return f"Error adding thread: {str(error)}"

def twist_threads_update(
    ctx: Context,
    id: int,
    actions: Optional[List[Dict[str, Any]]] = None,
    attachments: Optional[List[Dict[str, Any]]] = None,
    content: Optional[str] = None,
    direct_group_mentions: Optional[List[int]] = None,
    direct_mentions: Optional[List[int]] = None,
    title: Optional[str] = None
) -> Union[str, Dict[str, Any]]:
    """Updates an existing thread.

    Args:
        id: The id of the thread
        actions: List of action buttons to the thread
        attachments: List of attachments to the thread
        content: The content of the thread
        direct_group_mentions: The groups that are directly mentioned
        direct_mentions: The users that are directly mentioned
        title: The title of the thread
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Updating thread with ID: {id}")
        thread_data = twist_request("threads/update", params=params, token=token, method="POST")
        logger.info(f"Updated thread with ID: {id}")
        return thread_data
    except Exception as error:
        logger.error(f"Error updating thread: {error}")
        return f"Error updating thread: {str(error)}"

def twist_threads_remove(
    ctx: Context,
    id: int
) -> str:
    """Removes a thread.

    Args:
        id: The id of the thread
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Removing thread with ID: {id}")
        twist_request("threads/remove", params=params, token=token, method="POST")
        logger.info(f"Successfully removed thread with ID: {id}")
        return f"Successfully removed thread with ID: {id}"
    except Exception as error:
        logger.error(f"Error removing thread: {error}")
        return f"Error removing thread: {str(error)}"

def twist_threads_star(
    ctx: Context,
    id: int
) -> str:
    """Stars a thread.

    Args:
        id: The id of the thread
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Starring thread with ID: {id}")
        twist_request("threads/star", params=params, token=token, method="POST")
        logger.info(f"Successfully starred thread with ID: {id}")
        return f"Successfully starred thread with ID: {id}"
    except Exception as error:
        logger.error(f"Error starring thread: {error}")
        return f"Error starring thread: {str(error)}"

def twist_threads_unstar(
    ctx: Context,
    id: int
) -> str:
    """Unstars a thread.

    Args:
        id: The id of the thread
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Unstarring thread with ID: {id}")
        twist_request("threads/unstar", params=params, token=token, method="POST")
        logger.info(f"Successfully unstarred thread with ID: {id}")
        return f"Successfully unstarred thread with ID: {id}"
    except Exception as error:
        logger.error(f"Error unstarring thread: {error}")
        return f"Error unstarring thread: {str(error)}"

def twist_threads_pin(
    ctx: Context,
    id: int
) -> str:
    """Pins a thread.

    Args:
        id: The id of the thread
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Pinning thread with ID: {id}")
        twist_request("threads/pin", params=params, token=token, method="POST")
        logger.info(f"Successfully pinned thread with ID: {id}")
        return f"Successfully pinned thread with ID: {id}"
    except Exception as error:
        logger.error(f"Error pinning thread: {error}")
        return f"Error pinning thread: {str(error)}"

def twist_threads_unpin(
    ctx: Context,
    id: int
) -> str:
    """Unpins a thread.

    Args:
        id: The id of the thread
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Unpinning thread with ID: {id}")
        twist_request("threads/unpin", params=params, token=token, method="POST")
        logger.info(f"Successfully unpinned thread with ID: {id}")
        return f"Successfully unpinned thread with ID: {id}"
    except Exception as error:
        logger.error(f"Error unpinning thread: {error}")
        return f"Error unpinning thread: {str(error)}"

def twist_threads_move_to_channel(
    ctx: Context,
    id: int,
    to_channel: int
) -> str:
    """Moves the thread to a different channel.

    Args:
        id: The id of the thread
        to_channel: The target channel's id
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Moving thread with ID: {id} to channel: {to_channel}")
        twist_request("threads/move_to_channel", params=params, token=token, method="POST")
        logger.info(f"Successfully moved thread with ID: {id} to channel: {to_channel}")
        return f"Successfully moved thread with ID: {id} to channel: {to_channel}"
    except Exception as error:
        logger.error(f"Error moving thread: {error}")
        return f"Error moving thread: {str(error)}"

def twist_threads_get_unread(
    ctx: Context
) -> Union[str, List[Dict[str, Any]]]:
    """Gets unread threads in a workspace for the authenticated user.
    """
    token = ctx.request_context.lifespan_context.twist_token

    workspace_id = os.getenv("TWIST_WORKSPACE_ID")
    if not workspace_id:
        logger.error("TWIST_WORKSPACE_ID environment variable is required")
        return "Error: TWIST_WORKSPACE_ID environment variable is required"

    params = {"workspace_id": workspace_id}

    try:
        logger.info(f"Getting unread threads for workspace ID: {workspace_id}")
        unread_data = twist_request("threads/get_unread", params=params, token=token)

        if not unread_data:
            logger.info("No unread threads found")
            return "No unread threads found"

        logger.info(f"Retrieved {len(unread_data)} unread threads")
        return unread_data
    except Exception as error:
        logger.error(f"Error getting unread threads: {error}")
        return f"Error getting unread threads: {str(error)}"

def twist_threads_mark_read(
    ctx: Context,
    id: int,
    obj_index: int
) -> str:
    """Marks the thread as being read.

    Args:
        id: The id of the thread
        obj_index: The index of the last known read message
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Marking thread with ID: {id} as read up to comment index: {obj_index}")
        twist_request("threads/mark_read", params=params, token=token, method="POST")
        logger.info(f"Successfully marked thread with ID: {id} as read")
        return f"Successfully marked thread with ID: {id} as read up to comment index: {obj_index}"
    except Exception as error:
        logger.error(f"Error marking thread as read: {error}")
        return f"Error marking thread as read: {str(error)}"

def twist_threads_mark_unread(
    ctx: Context,
    id: int,
    obj_index: int
) -> str:
    """Marks the thread as being unread.

    Args:
        id: The id of the thread
        obj_index: The index of the last unread message. A value of -1 marks the whole thread as unread
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Marking thread with ID: {id} as unread from comment index: {obj_index}")
        twist_request("threads/mark_unread", params=params, token=token, method="POST")
        logger.info(f"Successfully marked thread with ID: {id} as unread")
        return f"Successfully marked thread with ID: {id} as unread from comment index: {obj_index}"
    except Exception as error:
        logger.error(f"Error marking thread as unread: {error}")
        return f"Error marking thread as unread: {str(error)}"

def twist_threads_mark_unread_for_others(
    ctx: Context,
    id: int,
    obj_index: int
) -> str:
    """Marks the thread as being unread for others.

    Args:
        id: The id of the thread
        obj_index: The index of the last unread message. A value of -1 marks the whole thread as unread
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Marking thread with ID: {id} as unread for others from comment index: {obj_index}")
        twist_request("threads/mark_unread_for_others", params=params, token=token, method="POST")
        logger.info(f"Successfully marked thread with ID: {id} as unread for others")
        return f"Successfully marked thread with ID: {id} as unread for others from comment index: {obj_index}"
    except Exception as error:
        logger.error(f"Error marking thread as unread for others: {error}")
        return f"Error marking thread as unread for others: {str(error)}"

def twist_threads_mark_all_read(
    ctx: Context,
    workspace_id: Optional[int] = None,
    channel_id: Optional[int] = None
) -> str:
    """Marks all threads in the workspace or channel as read.

    Args:
        workspace_id: The id of the workspace
        channel_id: The id of the channel
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    if not workspace_id and not channel_id:
        workspace_id = os.getenv("TWIST_WORKSPACE_ID")
        if not workspace_id:
            logger.error("Either workspace_id or channel_id is required")
            return "Error: Either workspace_id or channel_id is required"
        params["workspace_id"] = workspace_id

    try:
        if "channel_id" in params:
            logger.info(f"Marking all threads in channel ID: {params['channel_id']} as read")
        else:
            logger.info(f"Marking all threads in workspace ID: {params['workspace_id']} as read")

        twist_request("threads/mark_all_read", params=params, token=token, method="POST")

        if "channel_id" in params:
            logger.info(f"Successfully marked all threads in channel ID: {params['channel_id']} as read")
            return f"Successfully marked all threads in channel ID: {params['channel_id']} as read"
        else:
            logger.info(f"Successfully marked all threads in workspace ID: {params['workspace_id']} as read")
            return f"Successfully marked all threads in workspace ID: {params['workspace_id']} as read"
    except Exception as error:
        logger.error(f"Error marking all threads as read: {error}")
        return f"Error marking all threads as read: {str(error)}"

def twist_threads_clear_unread(
    ctx: Context
) -> str:
    """Clears unread threads in workspace.
    """
    token = ctx.request_context.lifespan_context.twist_token

    workspace_id = os.getenv("TWIST_WORKSPACE_ID")
    if not workspace_id:
        logger.error("TWIST_WORKSPACE_ID environment variable is required")
        return "Error: TWIST_WORKSPACE_ID environment variable is required"

    params = {"workspace_id": workspace_id}

    try:
        logger.info(f"Clearing unread threads for workspace ID: {workspace_id}")
        twist_request("threads/clear_unread", params=params, token=token, method="POST")
        logger.info("Successfully cleared unread threads")
        return "Successfully cleared unread threads"
    except Exception as error:
        logger.error(f"Error clearing unread threads: {error}")
        return f"Error clearing unread threads: {str(error)}"

def twist_threads_mute(
    ctx: Context,
    id: int,
    minutes: int
) -> Union[str, Dict[str, Any]]:
    """Mutes a thread for a number of minutes.

    Args:
        id: The id of the thread
        minutes: The number of minutes to mute the thread
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Muting thread with ID: {id} for {minutes} minutes")
        thread_data = twist_request("threads/mute", params=params, token=token, method="POST")
        logger.info(f"Successfully muted thread with ID: {id}")
        return thread_data
    except Exception as error:
        logger.error(f"Error muting thread: {error}")
        return f"Error muting thread: {str(error)}"

def twist_threads_unmute(
    ctx: Context,
    id: int
) -> Union[str, Dict[str, Any]]:
    """Unmutes a thread.

    Args:
        id: The id of the thread
    """
    all_params = locals()
    token = ctx.request_context.lifespan_context.twist_token
    params = {k: v for k, v in all_params.items() if k != 'ctx' and v is not None}

    try:
        logger.info(f"Unmuting thread with ID: {id}")
        thread_data = twist_request("threads/unmute", params=params, token=token, method="POST")
        logger.info(f"Successfully unmuted thread with ID: {id}")
        return thread_data
    except Exception as error:
        logger.error(f"Error unmuting thread: {error}")
        return f"Error unmuting thread: {str(error)}"
