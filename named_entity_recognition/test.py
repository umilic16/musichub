import spacy

nlp = spacy.load('.old/models/mh_ner/v2.2/model-best')
while True:
    text = input("Enter something: ")
    text = text.lower()
    if text == 'stop':
        break
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.label_, ent.text)