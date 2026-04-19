def is_song_in_dict(song_dict: dict, song_artist_tuple: tuple) -> bool:
    if len(song_dict) <= 15:
        try:
            song_dict[song_artist_tuple]
        except KeyError:
            return False
        return True