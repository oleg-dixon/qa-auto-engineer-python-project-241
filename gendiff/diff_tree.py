from typing import Any, Dict, List


def build_diff(
    data1: Dict[str, Any],
    data2: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """
    Constructs a tree of differences between two dictionaries.

    This function compares two dictionaries (`data1` and `data2`) and 
    generates a list of differences. Each difference is represented 
    as a dictionary with a status and, if applicable, old and new values.

    Args:
        data1 (Dict[str, Any]): The first dictionary to compare.
        data2 (Dict[str, Any]): The second dictionary to compare.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries representing
        the differences between the two input dictionaries.
"""
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        node = {'key': key}

        if key not in data1:
            node.update({
                'status': 'added',
                'value': data2[key]
            })
        elif key not in data2:
            node.update({
                'status': 'removed',
                'value': data1[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            node.update({
                'status': 'nested',
                'children': build_diff(data1[key], data2[key])
            })
        elif data1[key] != data2[key]:
            node.update({
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })
        else:
            node.update({
                'status': 'unchanged',
                'value': data1[key]
            })

        diff.append(node)

    return diff
