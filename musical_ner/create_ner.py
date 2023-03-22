import spacy
import json
from spacy.lang.en import English


def load_data(file):
    with open(file, "r", encoding='utf-8') as f:
        data = json.load(f)
    return (data)


def save_data(file, data):
    with open(file, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def create_training_data(file, type):
    patterns = []
    data = load_data(file)
    for item in data:
        pattern = {
            "label": type,
            "pattern": item
        }
        patterns.append(pattern)
    return (patterns)

# patterns = []
# patterns.extend(generate_patterns("data/albums.json", "ALBUM"))
# patterns.extend(generate_patterns("data/artists.json", "ARTIST"))
# patterns.extend(generate_patterns("data/genres.json", "GENRE"))
# patterns.extend(generate_patterns("data/instruments.json", "INSTRUMENT"))
# patterns.extend(generate_patterns("data/songs.json", "SONG"))

# save_data('data/all_patterns.json', patterns)

# data = load_data('data/all_patterns.json')
# generate_rules(data, "mh_entity_ruler")
try:
    nlp = spacy.load('models/mh_entity_ruler')
except Exception as ex:
    print(ex)
# while True:
#     text = input("Enter text to process: ")
#     if text.lower() == 'stop':
#         break
#     entities = nlp(text)
#     for entity in entities.ents:
#         print(entity.label_, entity.text)