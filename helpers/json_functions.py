import json
from os import path, makedirs

def load_data(file):
    if path.isfile(file):
        with open(file, "r", encoding='utf-8') as f:
            data = json.load(f)
        return (data)
    else:
        return None

def save_data(file, data):
    directory = path.dirname(file)
    if not path.exists(directory) and directory != '':
        makedirs(directory)
    with open(file, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)
