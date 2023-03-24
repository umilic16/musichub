import spacy

nlp = spacy.load('models/mh_ner/v1.0/model-best')
while True:
    text = input("Enter something: ")
    text = text.lower()
    if text == 'stop':
        break
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.label_, ent.text)