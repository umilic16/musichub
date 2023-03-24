from functions import get_music_info, play_song
from intent_recognition.neuralintents import GenericAssistant
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_trf")

def named_entity_recoqnition(message):
    doc = nlp(message)
    print(doc.ents)
    # displacy.serve(doc, style="ent")

def request_data(message):
    print("You triggered request_data")
    print(message)
    # Retrieve information about music topic using OpenAI API
    # info = get_music_info(message)

def play_music(message):
    print("You triggered play_music!")
    print(message)
    named_entity_recoqnition(message)
    # Extract song name from user input
    # song_name = extract_song_name(user_input)
    # Play song using YouTube API
    # link = play_song(song_name)
    # if link is not None:
    #     print(f"Playing {song_name}: {link}")
    # else:
    #     print("Sorry, I could not find that song on YouTube.")


mappings = {'request_data': request_data, 'play_music': play_music}
assistant = GenericAssistant(intent_methods=mappings, model_name="test_model", responses="training/data/responses.json")
assistant.load_model("training/models")


while True:
    # Receive input from user
    user_input = input("Enter a message: ")
    if user_input == "STOP":
        break
    else:
        # Use intent recognition model to determine user's intent
        response = assistant.request(user_input)
        if response:
            print(response)