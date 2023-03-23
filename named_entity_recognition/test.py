import spacy

nlp = spacy.load('named_entity_recognition/models/mh_ner/v0.1')
while True:
    text = input("Enter something: ")
    text = text.lower()
    if text == 'stop':
        break
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.label_, ent.text)