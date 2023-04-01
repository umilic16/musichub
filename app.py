from intent_recognition.neuralintents import GenericAssistant
import spacy
from flask import Flask, jsonify, request
import openai
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
from flask_cors import CORS

def named_entity_recoqnition(message):
    doc = ner_model(message)
    return doc.ents


def request_data(message):
    response = generate_response(message)
    return response


def play_music(message):
    entities = named_entity_recoqnition(message)
    if len(entities) == 0:
        # TO DO - Handle when no entities are found in user's input
        pass
    else:
        entities = ' '.join(str(ent) for ent in entities)
    link = search_youtube(entities)
    if link is not None:
        return {"type": "link", "data": link}
    else:
        return {"type": "data", "data": "Sorry, I could not find that song on YouTube."}


app = Flask(__name__)
CORS(app)

# Load the intent recognition model
mappings = {"request_data": request_data, "play_music": play_music}
ir_model = GenericAssistant(intent_methods=mappings, model_name="intent_recognition",
                            responses="intent_recognition/data/responses.json")
ir_model.load_model("intent_recognition/models", "intent_recognition")

# Load the named entity recognition model
ner_model = spacy.load(
    "named_entity_recognition/models/v3.2/model-best")

load_dotenv()
youtube_api_key = os.getenv("YOUTUBE_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

youtube = build("youtube", "v3", developerKey=youtube_api_key)

messages = [{"role": "system", "content": "You are an AI music assistant named MusicHub, an expert for music knowledge. You know everything about music (musicians, artists, songs, albums, composers, genres, instruments everything music-related), and you are designed to answer any music-related questions users may have. If the question is not music-related, you will respond with a message indicating that you are unable to provide a response."}]
# Function to generate a response from OpenAI API
def generate_response(prompt):
    """
    This function takes in a music related topic as input and returns
    information about that topic using the OpenAI API.
    """
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = messages,
    max_tokens=100,
    temperature=0.3,
    stream=True 
    )
    collected_messages = []
    # iterate through the stream of events
    for chunk in response:
        chunk_message = chunk['choices'][0]['delta']  # extract the message
        collected_messages.append(chunk_message)  # save the message

    full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
    messages.append({"role": "assistant", "content": full_reply_content})
    return {"type": "data", "data": full_reply_content}


# Function to search for a song on YouTube and return a link
def search_youtube(query):
    """
    This function takes in a song name as input and, searches youtube and returns the song
    url using the YouTube API.
    """
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=query,
        type="video",
    )
    response = request.execute()
    if response["items"]:
        video_id = response["items"][0]["id"]["videoId"]
        return f"https://www.youtube.com/watch?v={video_id}"
    else:
        return None

# Endpoint for handling all requests


@app.route("/", methods=["POST"])
def handle_request():
    # Get the user input from the JSON payload
    user_input = request.json.get("message")
    # Use intent recognition model to determine user"s intent
    response = ir_model.request(user_input)
    # Return the response to the user as a JSON object
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
