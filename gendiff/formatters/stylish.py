from typing import Any, Dict, List


def format_stylish(diff: List[Dict[str, Any]], depth: int = 0) -> str:
    """
    Formats the diff into a stylish, human-readable string with indentation 
    and nested structures.

    Args:
        diff (list): A list of dictionaries representing the diff data.
        depth (int): The current depth level for indentation.

    Returns:
        str: A stylishly formatted string representing the diff, with updates, 
             additions, removals, and changes.
"""
    indent = '    ' * depth
    lines = []
    
    for node in diff:
        key = node['key']
        status = node['status']
        
        if status == 'nested':
            lines.append(f"{indent}    {key}: {{")
            lines.append(format_stylish(node['children'], depth + 1))
            lines.append(f"{indent}    }}")
        elif status == 'changed':
            lines.append(
                f"{indent}  - "
                f"{key}: {format_value(node['old_value'], depth + 1)}"
                )
            lines.append(
                f"{indent}  + "
                f"{key}: {format_value(node['new_value'], depth + 1)}"
                )
        elif status == 'added':
            lines.append(
                f"{indent}  + "
                f"{key}: {format_value(node['value'], depth + 1)}"
                )
        elif status == 'removed':
            lines.append(
                f"{indent}  - "
                f"{key}: {format_value(node['value'], depth + 1)}"
                )
        else:
            lines.append(
                f"{indent}    "
                f"{key}: {format_value(node['value'], depth + 1)}"
                )

    if depth == 0:
        return '{\n' + '\n'.join(lines) + '\n}'
    return '\n'.join(lines)


def format_value(value: Any, depth: int) -> str:
    """
    Formats a value for display in the diff, with nested structures handled.

    Args:
        value (any): The value to be formatted.
        depth (int): The current depth level for indentation.

    Returns:
        str: A formatted string representation of the value.
    """
    if isinstance(value, dict):
        indent = '    ' * (depth + 1)
        lines = ['{']
        for k, v in value.items():
            lines.append(f"{indent}{k}: {format_value(v, depth + 1)}")
        lines.append('    ' * depth + '}')
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    return str(value)
