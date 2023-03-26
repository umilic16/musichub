import json
from os import path, makedirs
from typing import Union, Any

def load_data(file: str)-> Union[dict, None]:
    """Loads data from a JSON file.

    Args:
        file (str): The path to the JSON file to load.

    Returns:
        Union[dict, None]: A dictionary representing the loaded JSON data if the file exists, otherwise None.
    """
    if path.isfile(file):
        with open(file, "r", encoding='utf-8') as f:
            data = json.load(f)
        return (data)
    else:
        return None


def save_data(file: str, data: Any) -> None:
    """Saves data to a JSON file.

    Args:
        file (str): The path to the JSON file to save.
        data (Any): The data to save to the JSON file.

    Returns:
        None
    """
    directory = path.dirname(file)
    if not path.exists(directory) and directory != '':
        makedirs(directory)
    with open(file, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)
