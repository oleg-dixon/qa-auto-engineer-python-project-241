import argparse

from gendiff.generate_diff import generate_diff


def main() -> None:
    """
    Parses command-line arguments and generates a formatted diff 
    between two files.

    This function reads two file paths from the command line, compares
    their contents using the `generate_diff` function, and outputs 
    the result in the specified format (either 'json', 'plain', or 'stylish').
    If no format is specified, 'json' is used by default.

    Args:
        None (reads from command line arguments).

    Returns:
        None (prints the result of `generate_diff` to the console).
"""
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    # Positional arguments
    parser.add_argument(
        'first_file',
        metavar='first_file',
        help='The first file to compare.'
    )
    parser.add_argument(
        'second_file',
        metavar='second_file',
        help='The second file to compare.'
    )

    # Optional arguments
    parser.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        help='Set the format of the output (e.g., json, plain, stylish).',
        default='stylish'
    )

    args = parser.parse_args()
    print(generate_diff(
        args.first_file,
        args.second_file,
        args.format
    ))


if __name__ == '__main__':
    main()
