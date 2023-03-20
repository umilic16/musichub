# Set up OpenAI API client
import openai
openai.api_key = "YOUR_OPENAI_API_KEY_HERE"

# Set up YouTube API client
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

api_key = "YOUR_YOUTUBE_API_KEY_HERE"
youtube = build('youtube', 'v3', developerKey=api_key)


def get_music_info(topic):
    """
    This function takes in a music related topic as input and returns
    information about that topic using the OpenAI API.
    """
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Please provide some information about {topic}.",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    info = response.choices[0].text.strip()
    return info


def play_song(song_name):
    """
    This function takes in a song name as input and plays the song
    using the YouTube API.
    """
    try:
        # Search for song on YouTube
        search_response = youtube.search().list(
            q=song_name,
            type='video',
            part='id,snippet',
            maxResults=1
        ).execute()

        # Get video ID of first search result
        video_id = search_response['items'][0]['id']['videoId']

        # Construct YouTube link
        link = f'https://www.youtube.com/watch?v={video_id}'

        # Return link to video
        return link

    except HttpError as e:
        # Handle API errors
        print(f"An error occurred: {e}")
        return None
