<<<<<<< HEAD
# SpotLyrSearch
Displays lyrics of song you're listening to on Spotify in a tkinter window

Could work for other apps if you know the executable name and if the other apps put the song in their window title (plus some more editting of the code so that the song and artist are correctly assigned)

TO RUN SCRIPT:
1. Download zip file and extract into where you wish to save
2. Right click in folder and open in terminal
3. Use command 'uv run display_lyrics.py' in terminal (without single quotes)

If the instructions above don't work:
install all the libraries below
1. ```pip install pywin32```
2. ```pip install customtkinter```
3. ```pip install requests```
4. ```pip install psutil```
5. Get at least a semi recent python version (I use 3.11)


Requirements:
1. Spotify app (When playing a song, the title of the window needs to be of the form "{Artist} - {Song}" (spaces dont matter but the first dash needs to separate the artist from the song))
2. Windows
3. Python (uv may download this for you but I dont know how to check)
4. A functioning CPU

Current features:
1. The lyrics automatically change when the song changes
2. GUI is always on top of every other window (might add smthg to turn this at some point later)

Things I need to add later:
1. Add a script to store the lyrics of recent songs for some time so don't have to fetch lyrics everytime
2. Get and display thumbnail image in background
3. Add settings menu
4. Set spawn location at 3/4 of monitor resolution (currently at a fixed pixel value (2500 as I have thicc monitor))
5. Rewrite in C++ to solve dependency issues (not going to happen until after A levels)
    1. Replace polling with event when window name changes (no sense having a polling loop and also an event loop) - will likely be more efficient

idk if adding a license is the correct thing to do but i may asw. not like it affects anything
=======
# SpotLyrSearch
Displays lyrics of song you're listening to on Spotify in a tkinter window

Could work for other apps if you know the executable name and if the other apps put the song in their window title (plus some more editting of the code so that the song and artist are correctly assigned)

Requirements:
    Spotify app (When playing a song, the title of the window needs to be of the form "{Artist} - {Song}" (spaces dont matter but the first dash needs to separate the artist from the song))
    Windows
    Python
    A functioning CPU
    A display (if you dont have a display, how did you even find this page)

___________________________________
|To run app, run display_lyrics.py|
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
>>>>>>> a563494 (Initial commit)
