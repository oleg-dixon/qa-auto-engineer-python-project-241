import os
from pathlib import Path

import pytest

from gendiff.generate_diff import generate_diff


def get_fixture_path(file_name: str, file_format: str) -> Path:
    """
    Returns the path to the fixture file based on the file name and format.

    Args:
        file_name (str): The name of the file.
        file_format (str): The format of the file ('json', 'yml', or 'yaml').

    Returns:
        Path: The path to the fixture file.
    
    Raises:
        ValueError: If an unsupported file format is provided.
    """
    if file_format == 'json':
        return Path(__file__).parent / 'test_data' / file_name
    if file_format in ('yml', 'yaml'):
        return Path(__file__).parent / 'test_data' / file_name
    raise ValueError(f"Unsupported file format: {file_format}")


test_cases = ['yml', 'yaml', 'json']


@pytest.mark.parametrize('format', test_cases)
def test_generate_diff(format: str) -> None:
    """
    Test the `generate_diff` function with different file formats.

    Args:
        format (str): The file format to test with ('json', 'yml', or 'yaml').

    Raises:
        AssertionError: If the output does not match the expected result.
    """
    base_path = 'gendiff/tests/test_data'
    with open(os.path.join(base_path, 'expected_output.txt')) as f:
        expected = f.read()
    file1 = os.path.join(base_path, f'file1.{format}')
    file2 = os.path.join(base_path, f'file2.{format}')
    result = generate_diff(file1, file2)
    assert expected == result, f'Expected:\n{expected}\n\nGot:\n{result}'
