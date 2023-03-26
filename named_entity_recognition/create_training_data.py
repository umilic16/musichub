import random
from tqdm import tqdm
from spacy.tokens import DocBin
import spacy
import sys
sys.path.append('../')
from helpers.json_functions import load_data, save_data


patterns = [
    "Play",
    "Play",
    "Play",
    "Hello give me",
    "Play",
    "Can you play",
    "Play",
    "Play",
    "Give me some",
    "Hi, can u play",
    "Play",
    "Hello my friend, im fealing great today can u play",
    "Hello how are you doin, im here for some",
    "im here for",
    "Hi bro can u play",
    "Hi can you play me"
    "Play some music",
    "Hey Music Hub, gimme some",
    "Hey MusicHub, play",
    "I'm in the mood for some music. Can you play",
    "I'm feeling nostalgic. Can you play",
    "Hey Music Hub, can you play",
    "Hey MusicHub, can you play",
    "Can you play",
    "I'm in the mood for some",
    "Play some of",
    "Give me something",
    "Can you play some",
    "lets play some",
    "Gimme",
    "Gimme some",
    "I want to listen to",
    "Can you play some",
    "I'm feeling like some",
    "Can you put on some",
    "I'm in the mood for",
    "put some",
    "Yo music hub, play",
    "Sup music hub can u play",
    "whats up music hub play me",
    "hi music hub, lets hear",
    "i want",
    "i need"
    "give me some",
    "i wanna hear some",
    "lets hear a",
    "play",
    "Play",
    "play some",
    "Hi, play",
    "Hello, play",
    "Hi MusicHub! Can u play",
    "Hello musichub, play"
]

album_am = ["", "", "", "-", "-", "by", "from", ",", "by", "from"]
album_sm = ["", "", "-", ","]
album_s = ["", "", "", "album", "please"]

artist_p = ["", "", "", "", "", "popular", "new",
            "new popular", "fresh", "fire from", "good", "nice"]
artist_m = ["", "", "", "-", ",", "'s", "s"]
artist_sg = ["", "", "", "hit", "vibe", "tune", "songs",
             "hits", "tunes", "track", "tracks", "music", "please"]
artist_ss = ["", "", "", "song"]
artist_sa = ["", "", "", "album"]

genre_p = ["", "", "", "", "" "popular", "new", "new popular", "fresh", "top"]
genre_s = ["", "", "", "song", "hit", "album", "vibe", "tune", "songs", "hits",
           "albums", "tunes", "track", "tracks", "music", "genre", "genres", "please"]

instrument_s = ["", "", "", "vibe", "music", "sound", "music", "", ""]

song_mal = ["", "", "", "-", "-", "from", ",", "from"]
song_mar = ["", "", "", "-", "-", "by", "from", ",", "by", "from"]
song_s = ["", "", "", "song", "please"]


def generate_albums_td(albums_data: list, artists_data: list, songs_data: list) -> list:
    """
    Generates random text training data for albums based on a set of pre-defined patterns.

    Args:
    - albums_data (list): A list of albums.
    - artists_data (list): A list of artists.
    - songs_data (list): A list of songs.

    Returns:
    - A list of generated sentences along with their corresponding entities. Each entry is represented as a tuple
    containing the generated text and a dictionary with the entities represented as tuples containing the start
    and end positions of the entity in the generated text and the entity type (in this dataset all entities have type "MUSIC").
    """
    print("Generating albums data")
    data = []
    for album in tqdm(albums_data):
        pattern = random.choice(patterns)

        text = pattern + " "
        album_start = len(text)
        text += album
        album_end = len(text)

        entities = [(album_start, album_end, "MUSIC")]

        choice = random.randint(1, 3)
        """
            1 - album
            2 - album artist
            3 - album song
        """
        if choice == 1:
            pass
        elif choice == 2:
            artist = random.choice(artists_data)
            mid = random.choice(album_am)
            if mid:
                text += " " + mid + " "
                artist_start = len(text)
                text += artist
                artist_end = len(text)
                entities.append((artist_start, artist_end, "MUSIC"))
            else:
                text += " "
                artist_start = len(text)
                text += artist
                artist_end = len(text)
                entities.append((artist_start, artist_end, "MUSIC"))
        else:
            song = random.choice(songs_data)
            mid = random.choice(album_sm)
            if mid:
                text += " " + mid + " "
                song_start = len(text)
                text += song
                song_end = len(text)
                entities.append((song_start, song_end, "MUSIC"))
            else:
                text += " "
                song_start = len(text)
                text += song
                song_end = len(text)
                entities.append((song_start, song_end, "MUSIC"))

        sufix = random.choice(album_s)
        if sufix:
            text += " " + sufix

        result = [text, {"entities": entities}]
        # print(result)
        data.append(result)
    return data


def generate_artists_td(albums_data: list, artists_data: list, songs_data: list) -> list:
    """
    Generates random text training data for artists based on a set of pre-defined patterns.

    Args:
    - albums_data (list): A list of albums.
    - artists_data (list): A list of artists.
    - songs_data (list): A list of songs.

    Returns:
    - A list of generated sentences along with their corresponding entities. Each entry is represented as a tuple
    containing the generated text and a dictionary with the entities represented as tuples containing the start
    and end positions of the entity in the generated text and the entity type (in this dataset all entities have type "MUSIC").
    """
    print("Generating artists data")
    data = []
    for artist in tqdm(artists_data):
        pattern = random.choice(patterns)

        text = pattern + " "

        prefix = random.choice(artist_p)
        if prefix:
            text += prefix + " "

        artist_start = len(text)
        text += artist
        artist_end = len(text)

        entities = [(artist_start, artist_end, "MUSIC")]

        choice = random.randint(1, 3)
        """
        1 - artist
        2 - artist album
        3 - artist song
        """
        if choice == 1:
            sufix = random.choice(artist_sg)
            if sufix:
                text += " " + sufix
        elif choice == 2:
            album = random.choice(albums_data)
            mid = random.choice(artist_m)
            if mid:
                if mid == "'s" or mid == 's':
                    text += mid + " "
                else:
                    text += " " + mid + " "
                album_start = len(text)
                text += album
                album_end = len(text)
                entities.append((album_start, album_end, "MUSIC"))
            else:
                text += " "
                album_start = len(text)
                text += album
                album_end = len(text)
                entities.append((album_start, album_end, "MUSIC"))
            sufix = random.choice(artist_sa)
            if sufix:
                text += " " + sufix
        else:
            song = random.choice(songs_data)
            mid = random.choice(album_sm)
            if mid:
                text += " " + mid + " "
                song_start = len(text)
                text += song
                song_end = len(text)
                entities.append((song_start, song_end, "MUSIC"))
            else:
                text += " "
                song_start = len(text)
                text += song
                song_end = len(text)
                entities.append((song_start, song_end, "MUSIC"))
            sufix = random.choice(artist_ss)
            if sufix:
                text += " " + sufix

        result = [text, {"entities": entities}]
        # print(result)
        data.append(result)
    return data


def generate_genres_td(genres_data: list) -> list:
    """
    Generates random text training data for music genres based on a set of pre-defined patterns.

    Args:
    - genres_data (list): A list of genres.

    Returns:
    - A list of generated sentences along with their corresponding entities. Each entry is represented as a tuple
    containing the generated text and a dictionary with the entities represented as tuples containing the start
    and end positions of the entity in the generated text and the entity type (in this dataset all entities have type "MUSIC").
    """
    print("Generating genres data")
    data = []
    for genre in tqdm(genres_data):
        pattern = random.choice(patterns)

        text = pattern + " "

        prefix = random.choice(genre_p)
        if prefix:
            text += prefix + " "

        genre_start = len(text)
        text += genre
        genre_end = len(text)

        entities = [(genre_start, genre_end, "MUSIC")]

        sufix = random.choice(genre_s)
        if sufix:
            text += " " + sufix

        result = [text, {"entities": entities}]
        # print(result)
        data.append(result)
    return data


def generate_instruments_td(instruments_data: list) -> list:
    """
    Generates random text training data for instruments based on a set of pre-defined patterns.

    Args:
    - instruments_data (list): A list of instruments.

    Returns:
    - A list of generated sentences along with their corresponding entities. Each entry is represented as a tuple
    containing the generated text and a dictionary with the entities represented as tuples containing the start
    and end positions of the entity in the generated text and the entity type (in this dataset all entities have type "MUSIC").
    """
    print("Generating instruments data")
    data = []
    for instrument in tqdm(instruments_data):
        pattern = random.choice(patterns)

        text = pattern + " "

        instrument_start = len(text)
        text += instrument
        instrument_end = len(text)

        entities = [(instrument_start, instrument_end, "MUSIC")]

        sufix = random.choice(instrument_s)
        if sufix:
            text += " " + sufix

        result = [text, {"entities": entities}]
        # print(result)
        data.append(result)
    return data


def generate_songs_td(albums_data: list, artists_data: list, songs_data: list) -> list:
    """
    Generates random text training data for songs based on a set of pre-defined patterns.

    Args:
    - albums_data (list): A list of albums.
    - artists_data (list): A list of artists.
    - songs_data (list): A list of songs.

    Returns:
    - A list of generated sentences along with their corresponding entities. Each entry is represented as a tuple
    containing the generated text and a dictionary with the entities represented as tuples containing the start
    and end positions of the entity in the generated text and the entity type (in this dataset all entities have type "MUSIC").
    """
    print("Generating songs data")
    data = []
    for song in tqdm(songs_data):
        pattern = random.choice(patterns)

        text = pattern + " "

        song_start = len(text)
        text += song
        song_end = len(text)

        entities = [(song_start, song_end, "MUSIC")]

        choice = random.randint(1, 3)
        """
            1 - song
            2 - song album
            3 - song artist
        """
        if choice == 1:
            pass
        elif choice == 2:
            album = random.choice(albums_data)
            mid = random.choice(song_mal)
            if mid:
                text += " " + mid + " "
                album_start = len(text)
                text += album
                album_end = len(text)
                entities.append((album_start, album_end, "MUSIC"))
            else:
                text += " "
                album_start = len(text)
                text += album
                album_end = len(text)
                entities.append((album_start, album_end, "MUSIC"))
        else:
            artist = random.choice(artists_data)
            mid = random.choice(song_mar)
            if mid:
                text += " " + mid + " "
                artist_start = len(text)
                text += artist
                artist_end = len(text)
                entities.append((artist_start, artist_end, "MUSIC"))
            else:
                text += " "
                artist_start = len(text)
                text += artist
                artist_end = len(text)
                entities.append((artist_start, artist_end, "MUSIC"))

        sufix = random.choice(song_s)
        if sufix:
            text += " " + sufix
        result = [text, {"entities": entities}]
        # print(result)
        data.append(result)
    return data


def export_data_to_json(filepath: str, albums: list, artists: list, genres: list, instruments: list, songs: list) -> None:
    """
    Uses functions for generating training data for albums, artists, genres, instruments and songs, and appends it into an array.
    Shuffles the array containing all the training data and exports it as a JSON file to the specified file path.

    Args:
        filepath (str): The file path where the JSON file will be saved.
        albums: A list of albums.
        artists: A list of artists.
        genres: A list of genres.
        instruments: A list of instruments.
        songs: A list of songs.

    Returns:
        None
    """
    data = []
    data.append(generate_albums_td(albums, artists, songs))
    data.append(generate_artists_td(albums, artists, songs))
    data.append(generate_genres_td(genres))
    data.append(generate_instruments_td(instruments))
    data.append(generate_songs_td(albums, artists, songs))

    random.shuffle(data)
    save_data(filepath, data)
    print('Json data is saved and ready!')


def convert_to_spacy(json_file_path: str, spacy_file_path: str, data_start_pt: int, data_end_pt: int) -> None:
    """
    Converts the data in the given JSON file (if the file exists) to Spacy format and saves it to the specified file path.

    Args:
        json_file_path (str): The file path of the JSON file to be converted.
        spacy_file_path (str): The file path where the Spacy data will be saved.
        data_start_pt (int): The starting index of the data to be processed.
        data_end_pt (int): The ending index of the data to be processed.

    Returns:
        None
    """
    data = load_data(json_file_path)
    if data is not None:
        nlp = spacy.blank("en")
        db = DocBin()
        for text, annotations in tqdm(data[data_start_pt:data_end_pt]):
            doc = nlp.make_doc(text)
            ents = []
            for start, end, label in annotations["entities"]:
                span = doc.char_span(start, end, label=label)
                if span is not None:
                    ents.append(span)
            doc.ents = ents
            db.add(doc)
        db.to_disk(spacy_file_path)
        print('Spacy data is saved and ready!')


def split_train_val_data(filepath: str, split: float) -> tuple[list, list]:
    """
    Splits the data in the given file into training and validation sets, based on the specified split percentage.

    Args:
        filepath: The file path of the data file to be split.
        split: A float representing the percentage of data to be included in the training set.
            Must be a value between 0 and 1. If greater than 1, it will be interpreted as a percentage value.

    Returns:
        A tuple of two lists containing the training and validation data, respectively.
    """
    data = load_data(filepath)
    if split > 1:
        split /= 100
    n = int(len(data) * split)
    data_tr = data[0:n]
    data_val = data[n+1:]
    return data_tr, data_val


# albums_data_tr, albums_data_val = split_train_val_data(
#     'data/music_data/albums.json', 0.7)

# artists_data_tr, artists_data_val = split_train_val_data(
#     'data/music_data/artists.json', 0.7)

# genres_data_tr, genres_data_val = split_train_val_data(
#     'data/music_data/genres.json', 0.7)

# instruments_data_tr, instruments_data_val = split_train_val_data(
#     'data/music_data/instruments.json', 0.7)

# songs_data_tr, songs_data_val = split_train_val_data(
#     'data/music_data/songs.json', 0.7)


# export_data_to_json('data/training_data.json', albums_data_tr,
#                     artists_data_tr, genres_data_tr, instruments_data_tr, songs_data_tr)
# print('Saved training data\nConverting .json training data to .spacy format')
# convert_to_spacy('data/training_data.json',
#                  'data/training_data_v2.spacy', 0, 700000)


# export_data_to_json('data/validation_data.json', albums_data_val,
#                     artists_data_val, genres_data_val, instruments_data_val, songs_data_val)
# print('Saved validation data\nConverting .json validation data to .spacy format')
# convert_to_spacy('data/validation_data.json',
#                  'data/validation_data_v2.spacy', 0, 300000)
