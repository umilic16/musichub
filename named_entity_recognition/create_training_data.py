from helpers.json_functions import load_data, save_data
import random
from tqdm import tqdm
from spacy.tokens import DocBin
import spacy
import sys
sys.path.append('../')


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

"""
    choices:
    1 - album
    2 - album artist
    3 - album song
"""


def create_albums_text(album, artists_data, songs_data):
    choice = random.randint(1, 3)
    pattern = random.choice(patterns)

    text = pattern + " "
    album_start = len(text)
    text += album
    album_end = len(text)

    entities = [(album_start, album_end, "MUSIC")]

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
    print(result)
    return result


"""
    1 - artist
    2 - artist album
    3 - artist song
"""


def create_artists_text(albums_data, artist, songs_data):
    choice = random.randint(1, 3)
    pattern = random.choice(patterns)

    text = pattern + " "

    prefix = random.choice(artist_p)
    if prefix:
        text += prefix + " "

    artist_start = len(text)
    text += artist
    artist_end = len(text)

    entities = [(artist_start, artist_end, "MUSIC")]

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
    print(result)
    return result


def create_genres_text(genre):
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
    print(result)
    return result


def create_instruments_text(instrument):
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
    print(result)
    return result


"""
    1 - song
    2 - song album
    3 - song artist
"""


def create_songs_text(albums_data, artists_data, song):
    choice = random.randint(1, 3)
    pattern = random.choice(patterns)

    text = pattern + " "

    song_start = len(text)
    text += song
    song_end = len(text)

    entities = [(song_start, song_end, "MUSIC")]

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
    print(result)
    return result


def export_data_to_json(filepath, albums, artists, genres, instruments, songs):
    data = []
    print("Generating album data")
    for album in tqdm(albums):
        data.append(create_albums_text(album, artists, songs))
    print("Generating artist data")
    for artist in tqdm(artists):
        data.append(create_artists_text(albums, artist, songs))
    print("Generating genre data")
    for genre in tqdm(genres):
        data.append(create_genres_text(genre))
    print("Generating instrument data")
    for instrument in tqdm(instruments):
        data.append(create_instruments_text(instrument))
    print("Generating song data")
    for song in tqdm(songs):
        data.append(create_songs_text(albums, artists, song))

    random.shuffle(data)
    save_data(filepath, data)
    print('Json data is saved and ready!')


def convert_to_spacy(json_file_path, spacy_file_path, data_start_pt, data_end_pt):
    data = load_data(json_file_path)
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


def split_training_validation_data(filepath, split):
    data = load_data(filepath)
    if split > 1:
        split /= 100
    n = int(len(data) * split)
    data_tr = data[0:n]
    data_val = data[n+1:]
    return data_tr, data_val


# albums_data_tr, albums_data_val = split_training_validation_data(
#     'data/albums.json', 0.7)

# artists_data_tr, artists_data_val = split_training_validation_data(
#     'data/artists.json', 0.7)

# genres_data_tr, genres_data_val = split_training_validation_data(
#     'data/genres.json', 0.7)

# instruments_data_tr, instruments_data_val = split_training_validation_data(
#     'data/instruments.json', 0.7)

# songs_data_tr, songs_data_val = split_training_validation_data(
#     'data/songs.json', 0.7)

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
