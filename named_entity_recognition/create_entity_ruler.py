import spacy
import json
from spacy.lang.en import English

"""
    modified version of this code: https://github.com/wjbmattingly/ner_youtube
    for creating an entity ruler in spacy
"""

def load_data(file):
    with open(file, "r", encoding='utf-8') as f:
        data = json.load(f)
    return (data)


def save_data(file, data):
    with open(file, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def generate_patterns(file, type):
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


# def test_model(model, text):
#     doc = model(text)
#     results = []
#     for ent in doc.ents:
#         results.append(ent.text)
#     return (results)


# patterns = generate_patterns('data/albums.json', "ALBUM")
# print (patterns[:10])

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