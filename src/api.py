#!/usr/bin/env python3

import os
import logging
import requests

logger = logging.getLogger("twist-mcp-server")

def get_api_client():
    """
    Initialize and return the Twist API token.

    Returns:
        str: Twist API token

    Raises:
        ValueError: If TWIST_API_TOKEN environment variable is not set
    """
    # Check for API token
    TWIST_API_TOKEN = os.getenv("TWIST_API_TOKEN")
    if not TWIST_API_TOKEN:
        logger.error("TWIST_API_TOKEN environment variable is required")
        raise ValueError("TWIST_API_TOKEN environment variable is required")

    logger.info("Twist API token initialized successfully")
    return TWIST_API_TOKEN

def twist_request(endpoint, params=None, token=None, method="GET"):
    """
    Make an API request to Twist.

    Args:
        endpoint (str): API endpoint to call (without the base URL)
        params (dict, optional): Dictionary of parameters to include in the request
        token (str, optional): Authentication token (if None, uses the one from get_api_client)
        method (str, optional): HTTP method to use (default: "GET")

    Returns:
        dict: Response data as a dictionary

    Raises:
        Exception: If the API request fails
    """
    if token is None:
        token = get_api_client()

    base_url = "https://api.twist.com/api/v3/"
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{base_url}{endpoint}"

    try:
        if method == "GET":
            response = requests.get(url, params=params, headers=headers)
        elif method == "POST":
            response = requests.post(url, data=params, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        response.raise_for_status()  # Raise an exception for 4XX/5XX responses
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Twist API request failed: {e}")
        raise
