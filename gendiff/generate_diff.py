
from gendiff.diff_tree import build_diff
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.parsers import load_file


def generate_diff(file1: str, file2: str, format_name: str = 'stylish') -> str:
    """
    Generates a formatted diff between two files based on the given format.

    This function compares the contents of two files and returns a diff 
    formatted in one of three formats: 'stylish', 'plain', or 'json'. If no 
    format is specified, 'stylish' is used by default.

    Args:
        file1 (str): The path to the first file.
        file2 (str): The path to the second file.
        format_name (str, optional): The format for the diff output. Can be 
                                     'stylish', 'plain', or 'json'. Defaults 
                                     to 'stylish'.

    Returns:
        str: A string representing the differences between the two files in 
             the specified format.

    Raises:
        ValueError: If an unsupported format is provided.
"""
    data1 = load_file(file1) or {}
    data2 = load_file(file2) or {}

    if not data1 and not data2:
        if format_name == 'stylish':
            return "{}"
        return "{}"

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    raise ValueError(f"Unsupported format: {format_name}")
