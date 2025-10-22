import json
from typing import Any


def parse_json(data: str) -> Any:
    """
    Parses a JSON string into a Python dictionary.

    Args:
        data (str): The JSON string to parse.

    Returns:
        Any: The parsed Python object (usually dict or list).

    Raises:
        ValueError: If the JSON is invalid.
    """
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")


def load_json(file_path: str) -> Any:
    """
    Reads and parses a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        Any: The parsed Python object (usually dict or list).

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file's content is not valid JSON.
    """
    with open(file_path, 'r') as f:
        return parse_json(f.read())
