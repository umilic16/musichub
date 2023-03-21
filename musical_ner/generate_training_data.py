import spacy
import json
import random
from spacy.lang.en import English
from spacy.pipeline import EntityRuler

def load_data(file):
    with open(file, "r") as f:
        data = json.load(f)
    return (data)

def save_data(file, data):
    with open (file, "w") as f:
        json.dump(data, f)

def create_training_data(file, type):
    patterns = []
    for item in file:
        pattern = {
                    "label": type,
                    "pattern": item
                    }
        patterns.append(pattern)
    return (patterns)

def generate_rules(patterns, model):
    nlp = English()
    ruler = EntityRuler(nlp)
    ruler.add_patterns(patterns)
    nlp.add_pipe(ruler)
    nlp.to_disk(f"models/{model}")

def test_model(model, text):
    doc = model(text)
    results = []
    for ent in doc.ents:
        results.append(ent.text)
    return (results)

patterns = create_training_data("data/artists.json", "ARTIST")
# print (patterns)
generate_rules(patterns, "musical_ner")