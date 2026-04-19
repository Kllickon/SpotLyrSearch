import get_song_artist
import time

def check_song_once() -> bool:
    old_song_artist_tuple = get_song_artist.get_song_artist_func()
    while get_song_artist.get_song_artist_func() == old_song_artist_tuple:
        time.sleep(1)
        # print(old_song_artist_tuple)
    return True
