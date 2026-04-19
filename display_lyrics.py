import customtkinter as ctk
import tkinter.font as tkFont
from get_lyrics import get_lyrics
from get_song_artist import get_song_artist_func
import threading
from check_same_song import check_song_once
from song_cache import is_song_in_dict

song_dict = {}

signal_event = threading.Event()

song_artist_tuple = get_song_artist_func()
print(song_artist_tuple)
song = song_artist_tuple[0]
artist = song_artist_tuple[1]
lyrics = get_lyrics(song, artist)


def check_song_inf():
    while True:
        if check_song_once():
            # print("SONG CHANGED")
            signal_event.set()

def recieve_song_change():
    global song_artist_tuple, song, artist, lyrics

    if signal_event.is_set():
        song_artist_tuple = get_song_artist_func()
        song = song_artist_tuple[0]
        artist = song_artist_tuple[1]

        if is_song_in_dict(song_dict, song_artist_tuple) == False:
            lyrics = get_lyrics(song, artist)  
            print("got em!")
        else:
            lyrics = song_dict[song_artist_tuple]
        song_dict[song_artist_tuple] = lyrics
        for k, v in song_dict.items():
            print(k)
        root.title(f"{song} - {artist}")
        textbox.configure(state="normal")
        textbox.delete("0.0", "end")
        textbox.insert("0.0", lyrics)
        textbox.configure(state="disabled")
        
        # print("UPDATED GUI")

        signal_event.clear()

def poll_event():
    recieve_song_change()
    root.after(100, poll_event)

threading.Thread(target=check_song_inf, daemon=True).start()

root = ctk.CTk(fg_color="#3B1465")

screen_width, screen_height =  root.winfo_screenwidth(), root.winfo_screenheight()

width = 600
height = 600

spawn_x = int(screen_width*0.75 - width*0.5)
spawn_y = int(screen_height*0.5 - height*0.5)
# print(spawn_y)

root.title(f"{song} - {artist}")
root.geometry(f"{width}x{height}+{spawn_x}+{spawn_y}")
root.attributes("-topmost", True)

font_path = "alata-regular.ttf"
tkFont.Font(root, name="Alata", size=35)

textbox = ctk.CTkTextbox(
    root, wrap="word", fg_color="#8050D8", 
    border_width=20, border_color="#3B1465", 
    font=ctk.CTkFont(family="Alata", size=35), 
    corner_radius=50
)

textbox.pack(fill="both", expand=True)
textbox.insert("0.0", lyrics)
textbox.configure(state="disabled")

poll_event()
# print(song_dict)
root.mainloop()