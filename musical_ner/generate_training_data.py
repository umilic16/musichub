import spacy
import json
import random
from spacy.lang.en import English
from spacy.pipeline import EntityRuler


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


def generate_rules(patterns, model):
    nlp = English()
    ruler = nlp.add_pipe("entity_ruler")
    # print(ruler)
    ruler.add_patterns(patterns)
    nlp.to_disk(f"models/{model}")


def test_model(model, text):
    doc = model(text)
    results = []
    for ent in doc.ents:
        results.append(ent.text)
    return (results)


# patterns = create_training_data('data/albums.json', "ALBUM")
# print (patterns[:10])
# patterns = []
# patterns.extend(create_training_data("data/albums.json", "ALBUM"))
# patterns.extend(create_training_data("data/artists.json", "ARTIST"))
# patterns.extend(create_training_data("data/genres.json", "GENRE"))
# patterns.extend(create_training_data("data/instruments.json", "INSTRUMENT"))
# patterns.extend(create_training_data("data/songs.json", "SONG"))

# save_data('data/all_patterns.json', patterns)
data = load_data('data/all_patterns.json')
generate_rules(data, "musical_ner")
