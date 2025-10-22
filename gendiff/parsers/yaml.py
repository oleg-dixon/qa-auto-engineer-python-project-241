from typing import Any

import yaml


def parse_yaml(data: str) -> Any:
    """
    Parses a YAML string into a Python dictionary.

    Args:
        data (str): The YAML string to parse.

    Returns:
        Any: The parsed Python object (usually dict or list).

    Raises:
        ValueError: If the YAML is invalid.
    """
    try:
        return yaml.safe_load(data)
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML: {e}")


def load_yaml(file_path: str) -> Any:
    """
    Reads and parses a YAML file.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        Any: The parsed Python object (usually dict or list).

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file's content is not valid YAML.
    """
    with open(file_path, 'r') as f:
        return parse_yaml(f.read())
