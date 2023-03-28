from intent_recognition.neuralintents import GenericAssistant
import spacy
from flask import Flask, jsonify, request
import openai
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os


def named_entity_recoqnition(message):
    doc = ner_model(message)
    return doc.ents


def request_data(message):
    response = generate_response(message)
    return response


def play_music(message):
    entities = named_entity_recoqnition(message)
    link = search_youtube(entities)
    if link is not None:
        print(f"Playing {entities}: {link}")
    else:
        print("Sorry, I could not find that song on YouTube.")

    return "Playing music"


app = Flask(__name__)

# Load the intent recognition model
mappings = {"request_data": request_data, "play_music": play_music}
ir_model = GenericAssistant(intent_methods=mappings, model_name="intent_recognition",
                            responses="intent_recognition/data/responses.json")
ir_model.load_model("intent_recognition/models", "intent_recognition")

# Load the named entity recognition model
ner_model = spacy.load(
    "named_entity_recognition/models/mh_ner/v2.2/model-best")

load_dotenv()
youtube_api_key = os.getenv("YOUTUBE_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

youtube = build("youtube", "v3", developerKey=youtube_api_key)

# Function to generate a response from OpenAI API


def generate_response(prompt):
    """
    This function takes in a music related topic as input and returns
    information about that topic using the OpenAI API.
    """
    # prompt = f'As an AI music assistant named MusicHub, I am designed to answer any music-related questions you may have. Please provide a clear and specific question or topic related to music in the prompt below. If the prompt is not music-related, I will respond with a message indicating that I am unable to provide a response. Here is the user\'s question: "{prompt}"'

    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )
        # print(response.choices[0].text)
        return response.choices[0].text
    except Exception as e:
        print("Error:", e)


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
    user_input = request.json.get("input")
    # Use intent recognition model to determine user"s intent
    response = ir_model.request(user_input)
    # Return the response to the user as a JSON object
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
