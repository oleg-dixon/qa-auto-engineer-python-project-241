import json
from typing import Dict


def format_json(diff: Dict) -> str:
    """
    Converts the given diff data into a formatted JSON string.

    Args:
        diff (dict): A dictionary containing the diff data to be formatted.

    Returns:
        str: A JSON string representation of the diff with an indentation 
             of 2 spaces.
"""
    return json.dumps(diff, indent=2)