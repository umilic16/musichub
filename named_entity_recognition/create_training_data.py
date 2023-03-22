import json
import random


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
def create_albums_text(albums_data, artists_data, songs_data):
    choice = random.randint(1, 3)
    pattern = random.choice(patterns)
    album = random.choice(albums_data)

    text = pattern + " "
    album_start = len(text)
    text += album
    album_end = len(text)

    entities = [(album_start, album_end, "ALBUM")]

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
            entities.append((artist_start, artist_end, "ARTIST"))
        else:
            text += " "
            artist_start = len(text)
            text += artist
            artist_end = len(text)
            entities.append((artist_start, artist_end, "ARTIST"))
    else:
        song = random.choice(songs_data)
        mid = random.choice(album_sm)
        if mid:
            text += " " + mid + " "
            song_start = len(text)
            text += song
            song_end = len(text)
            entities.append((song_start, song_end, "SONG"))
        else:
            text += " "
            song_start = len(text)
            text += song
            song_end = len(text)
            entities.append((song_start, song_end, "SONG"))

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
def create_artists_text(albums_data, artists_data, songs_data):
    choice = random.randint(1, 3)
    pattern = random.choice(patterns)
    artist = random.choice(artists_data)

    text = pattern + " "

    prefix = random.choice(artist_p)
    if prefix:
        text += prefix + " "

    artist_start = len(text)
    text += artist
    artist_end = len(text)

    entities = [(artist_start, artist_end, "ARTIST")]

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
            entities.append((album_start, album_end, "ALBUM"))
        else:
            text += " "
            album_start = len(text)
            text += album
            album_end = len(text)
            entities.append((album_start, album_end, "ALBUM"))
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
            entities.append((song_start, song_end, "SONG"))
        else:
            text += " "
            song_start = len(text)
            text += song
            song_end = len(text)
            entities.append((song_start, song_end, "SONG"))

    sufix = random.choice(artist_ss)
    if sufix:
        text += " " + sufix

    result = [text, {"entities": entities}]
    # print(result)
    return result


def create_genres_text(genres_data):
    pattern = random.choice(patterns)
    genre = random.choice(genres_data)

    text = pattern + " "

    prefix = random.choice(genre_p)
    if prefix:
        text += prefix + " "

    genre_start = len(text)
    text += genre
    genre_end = len(text)

    entities = [(genre_start, genre_end, "GENRE")]

    sufix = random.choice(genre_s)
    if sufix:
        text += " " + sufix

    result = [text, {"entities": entities}]
    # print(result)
    return result


def create_instruments_text(instruments_data):
    pattern = random.choice(patterns)
    instrument = random.choice(instruments_data)

    text = pattern + " "

    instrument_start = len(text)
    text += instrument
    instrument_end = len(text)

    entities = [(instrument_start, instrument_end, "INSTRUMENT")]

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
def create_songs_text(albums_data, artists_data, songs_data):
    choice = random.randint(1, 3)
    pattern = random.choice(patterns)
    song = random.choice(songs_data)

    text = pattern + " "

    song_start = len(text)
    text += song
    song_end = len(text)

    entities = [(song_start, song_end, "SONG")]

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
            entities.append((album_start, album_end, "ALBUM"))
        else:
            text += " "
            album_start = len(text)
            text += album
            album_end = len(text)
            entities.append((album_start, album_end, "ALBUM"))
    else:
        artist = random.choice(artists_data)
        mid = random.choice(song_mar)
        if mid:
            text += " " + mid + " "
            artist_start = len(text)
            text += artist
            artist_end = len(text)
            entities.append((artist_start, artist_end, "ARTIST"))
        else:
            text += " "
            artist_start = len(text)
            text += artist
            artist_end = len(text)
            entities.append((artist_start, artist_end, "ARTIST"))
    
    sufix = random.choice(song_s)
    if sufix:
        text += " " + sufix
    result = [text, {"entities": entities}]
    # print(result)
    return result

albums_data = load_data('data/albums.json')
artists_data = load_data('data/artists.json')
genres_data = load_data('data/genres.json')
instruments_data = load_data('data/instruments.json')
songs_data = load_data('data/songs.json')

data = []
for i in range(300000):
    data.append(create_albums_text(albums_data, artists_data, songs_data))
    data.append(create_artists_text(albums_data, artists_data, songs_data))
    data.append(create_songs_text(albums_data,artists_data,songs_data))
    if i % 3 == 0:
        data.append(create_genres_text(genres_data))
    if i % 10 == 0:
        data.append(create_instruments_text(instruments_data))

# print(data)
save_data('data/training_data.json', data)