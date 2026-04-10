import win32gui
import win32process
import psutil

def find_spotify_window():
    result = []

    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                proc = psutil.Process(pid)
                if proc.name().lower() == "spotify.exe":
                    title = win32gui.GetWindowText(hwnd)
                    result.append((hwnd, title))
            except psutil.NoSuchProcess:
                pass

    win32gui.EnumWindows(enum_handler, None)
    return result

def check_index_error():
    try:
        find_spotify_window()[0][1]
    except IndexError:
        print("Spotify aint open")
        quit()

def find_dash(song_artist):
    counter = 0
    for i in song_artist:
        if i == "-":
            break

        counter += 1
    return counter

def split_song_artist(song_artist, counter):
    artist = song_artist[:counter].strip()
    song = song_artist[counter + 1:].strip()
    return (song, artist)

def main():
    check_index_error()
    song_artist = find_spotify_window()[0][1]
    counter = find_dash(song_artist)
    song_artist_tuple = split_song_artist(song_artist, counter)
    # print(song_artist_tuple)
    # print(f"song: {song_artist_tuple[0]}")
    # print(f"artist: {song_artist_tuple[1]}")
    return song_artist_tuple
    
# main()