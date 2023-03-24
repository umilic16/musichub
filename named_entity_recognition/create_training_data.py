import json
import random
from tqdm import tqdm
from spacy.tokens import DocBin
import spacy

def load_data(file):
    with open(file, "r", encoding='utf-8') as f:
        data = json.load(f)
    return (data)

def save_data(file, data):
    with open(file, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)


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
    # print(result)
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
    # print(result)
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
    # print(result)
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
    # print(result)
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
    # print(result)
    return result


# albums_data = load_data('data/albums.json')
# n = int(len(albums_data)*0.70)
# albums_data_tr = albums_data[0:n]
# albums_data_val = albums_data[n+1:]

# artists_data = load_data('data/artists.json')
# n = int(len(artists_data)*0.70)
# artists_data_tr = artists_data[0:n]
# artists_data_val = artists_data[n+1:]

# genres_data = load_data('data/genres.json')
# n = int(len(genres_data)*0.70)
# genres_data_tr = genres_data[0:n]
# genres_data_val = genres_data[n+1:]

# instruments_data = load_data('data/instruments.json')
# n = int(len(instruments_data)*0.70)
# instruments_data_tr = instruments_data[0:n]
# instruments_data_val = instruments_data[n+1:]

# songs_data = load_data('data/songs.json')
# n = int(len(songs_data)*0.70)
# songs_data_tr = songs_data[0:n]
# songs_data_val = songs_data[n+1:]

# data = []
# print("Generating album training examples")
# for album in tqdm(albums_data_tr):
#     data.append(create_albums_text(album, artists_data_tr, songs_data_tr))
# print("Generating artist training examples")
# for artist in tqdm(artists_data_tr):
#     data.append(create_artists_text(albums_data_tr, artist, songs_data_tr))
# print("Generating song training examples")
# for song in tqdm(songs_data_tr):
#     data.append(create_songs_text(albums_data_tr,artists_data_tr,song))
# print("Generating genre training examples")
# for genre in tqdm(genres_data_tr):
#         data.append(create_genres_text(genre))
# print("Generating instrument training examples")
# for instrument in tqdm(instruments_data_tr):
#         data.append(create_instruments_text(instrument))

# print('Saving training data')
# random.shuffle(data)
# save_data('data/training_data_v2.json', data)
# print('Saved training data\nConverting .json training data to .spacy format')

data = load_data('data/training_data.json')

nlp = spacy.blank("en")
db = DocBin()
for text, annotations in tqdm(data[:700000]):
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annotations["entities"]:
        span = doc.char_span(start, end, label=label)
        if span is not None:
            ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("data/training_data.spacy")
print('training_data.spacy is saved and ready!')


# data = []
# print("Generating album validation examples")
# for album in tqdm(albums_data_val):
#     data.append(create_albums_text(album, artists_data_val, songs_data_val))
# print("Generating artist validation examples")
# for artist in tqdm(artists_data_val):
#     data.append(create_artists_text(albums_data_val, artist, songs_data_val))
# print("Generating song validation examples")
# for song in tqdm(songs_data_val):
#     data.append(create_songs_text(albums_data_val,artists_data_val,song))
# print("Generating genre validation examples")
# for genre in tqdm(genres_data_val):
#         data.append(create_genres_text(genre))
# print("Generating instrument validation examples")
# for instrument in tqdm(instruments_data_val):
#         data.append(create_instruments_text(instrument))

# print('Saving validation data')
# random.shuffle(data)
# save_data('data/validation_data.json', data)
# print('Saved validation data\nConverting .json validation data to .spacy format')

data = load_data('data/validation_data.json')
db = DocBin()
for text, annotations in tqdm(data[:300000]):
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annotations["entities"]:
        span = doc.char_span(start, end, label=label)
        if span is not None:
            ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("data/validation_data.spacy")
print('validation_data.spacy is saved and ready!')