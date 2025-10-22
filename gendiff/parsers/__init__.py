import json
from pathlib import Path
from typing import Union

import yaml


def parse_content(content: str, extension: str) -> Union[dict, list]:
    """
    Parses the content of a file based on its extension.

    Args:
        content (str): The content of the file as a string.
        extension (str): The file extension (e.g., '.json', '.yaml', '.yml').

    Returns:
        Union[dict, list]: The parsed content as a dictionary (for JSON/YAML) 
        or a list (for YAML).
    
    Raises:
        ValueError: If the file extension is unsupported.
"""
    if extension == '.json':
        return json.loads(content)
    elif extension in ('.yaml', '.yml'):
        return yaml.safe_load(content)
    raise ValueError(f"Unsupported file extension: {extension}")


FIXTURES_DIR = Path(__file__).resolve().parent.parent / 'tests' / 'fixtures'


def load_file(path: str) -> Union[dict, list]:
    """
    Loads a file's content and parses it based on its extension.

    Args:
        path (str): The file path to load and parse.

    Returns:
        Union[dict, list]: The parsed content of the file.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If there's an error reading or parsing the file.
    """
    path = Path(path).expanduser()

    if path.exists():
        actual_path = path.resolve()
    else:
        fixture_path = FIXTURES_DIR / path
        if fixture_path.exists():
            actual_path = fixture_path.resolve()
        else:
            raise FileNotFoundError(f"File not found: {path}")

    try:
        content = actual_path.read_text(encoding='utf-8')
        return parse_content(content, actual_path.suffix)
    except Exception as e:
        raise ValueError(f"Error reading {actual_path}: {str(e)}")
