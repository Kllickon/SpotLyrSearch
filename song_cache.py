def is_song_in_dict(song_dict: dict, song_artist_tuple: tuple) -> int:
    try:
        song_dict[song_artist_tuple]
        print("0")
        return 0 #Song in dict
    except KeyError: #Song not in dict
        if len(song_dict) > 15:
            print("1")
            return 1