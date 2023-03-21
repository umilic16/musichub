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
generate_rules(patterns, "musical_ner")
# print (patterns)

nlp = spacy.load("models/musical_ner")
ie_data = {}
with open ("data/training_data.txt", "r")as f:
    text = f.read()
    chapters = text.split("CHAPTER")[1:]
    for chapter in chapters:
        chapter_num, chapter_title = chapter.split("\n\n")[0:2]
        chapter_num = chapter_num.strip()
        segments = chapter.split("\n\n")[2:]
        hits = []
        for segment in segments:
            segment = segment.strip()
            segment = segment.replace("\n", " ")
            results = test_model(nlp, segment)
            for result in results:
                hits.append(result)
        ie_data[chapter_num] = hits

save_data("data/result.json", ie_data)