import customtkinter as ctk
from get_lyrics import get_lyrics
from get_song_artist import main
import threading
from check_same_song import check_song_once

signal_event = threading.Event()

song_artist_tuple = main()
song = song_artist_tuple[0]
artist = song_artist_tuple[1]
lyrics = get_lyrics(song, artist)

def check_song_inf():
    while True:
        if check_song_once():   # assuming this returns True when song changes
            print("SONG CHANGED")
            signal_event.set()

def recieve_song_change():
    global song_artist_tuple, song, artist, lyrics

    if signal_event.is_set():
        song_artist_tuple = main()
        song = song_artist_tuple[0]
        artist = song_artist_tuple[1]
        lyrics = get_lyrics(song, artist)

        print("UPDATED GUI")

        # Update GUI safely
        root.title(f"{song} - {artist}")
        textbox.configure(state="normal")
        textbox.delete("0.0", "end")
        textbox.insert("0.0", lyrics)
        textbox.configure(state="disabled")

        signal_event.clear()

def poll_event():
    recieve_song_change()
    root.after(100, poll_event)

# ---------------- GUI ----------------

width = 600
height = 600
spawn_x = 2500
spawn_y = 300

threading.Thread(target=check_song_inf, daemon=True).start()

root = ctk.CTk(fg_color="#3B1465")
root.title(f"{song} - {artist}")
root.geometry(f"{width}x{height}+{spawn_x}+{spawn_y}")
root.attributes("-topmost", True)

font=('Alata', 35)

textbox = ctk.CTkTextbox(
    root, wrap="word", fg_color="#8050D8",
    border_width=20, border_color="#3B1465",
    font=ctk.CTkFont(family=font[0], size=font[1]),
    corner_radius=50
)
textbox.pack(fill="both", expand=True)
textbox.insert("0.0", lyrics)
textbox.configure(state="disabled")

poll_event()
root.mainloop()
