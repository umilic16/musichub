import spacy

data = {
    "song_request": ["Can you play Bohemian Rhapsody by Queen?",
                     "I would like 'Shape of You' by Ed Sheeran.",
                     "Play eminem lose yourself",
                     "Can you add Stairway to Heaven by Led Zeppelin to the playlist?",
                     "Can you play 'Sweet Child O' Mine' by Guns N' Roses next?",
                     "I request anderson paak come down",
                     "Could you please play 'Don't Stop Believin'' by Journey?",
                     "I want to hear Eye of the Tiger by Survivor.",
                     "Can you play 'Smells Like Teen Spirit' by Nirvana?",
                     "Can you add 'Livin' on a Prayer' by Bon Jovi to the playlist?",
                     "Please play 'I Will Always Love You' by Whitney Houston."],
    "data_request": ["Who is mozzart",
                     "What do you know about Method Man",
                     "Who is the most successful musician",
                     "Can you tell me more about the life of Freddie Mercury?",
                     "What are some of the biggest hits from Michael Jackson?",
                     "Who is the lead guitarist of Guns N' Roses?",
                     "What was the first album released by Led Zeppelin?",
                     "Can you provide me with information about the origins of hip hop?",
                     "What is the most popular genre of music in the United States?",
                     "Who was the first female rapper to win a Grammy award?",
                     "What was the name of Prince's backup band?",
                     "What inspired the Beatles to write 'Let It Be'?",
                     "Can you tell me more about the history of the Rolling Stones?"]
}


# see github repo for examples on sentence-transformers and Huggingface
nlp = spacy.load('en_core_web_trf')
nlp.add_pipe("text_categorizer",
             config={
                 "data": data,
                 "model": "spacy"
             }
             )

print(nlp("Play me an Eminem song")._.cats)
print(nlp("Method man hit")._.cats)
print(nlp("Best lil baby song")._.cats)
