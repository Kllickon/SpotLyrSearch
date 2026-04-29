# SpotLyrSearch
Displays lyrics of song you're listening to on Spotify in a tkinter window

Could work for other apps if you know the executable name and if the other apps put the song in their window title (plus some more editting of the code so that the song and artist are correctly assigned)

TO RUN SCRIPT:
1. Install Python
2. Download zip file and extract into where you wish to save
3. Right click in folder and open in terminal
4. ```pip install uv```
5. Use command 'uv run display_lyrics.py' in terminal (without single quotes)

If the instructions above don't work:
install all the libraries below
1. ```pip install pywin32```
2. ```pip install customtkinter```
3. ```pip install requests```
4. ```pip install psutil```


Requirements:
1. Spotify app (When playing a song, the title of the window needs to be of the form "{Artist} - {Song}" (spaces dont matter but the first dash needs to separate the artist from the song))
2. Windows
3. Python (uv may download this for you but I dont know how to check)
4. A functioning CPU

Current features:
1. The lyrics automatically change when the song changes
2. GUI is always on top of every other window (might add smthg to turn this at some point later)
3. Window now spawns halfway down and 3/4 across monitor (means resolution and aspect ratio taken into account)
4. There is a cache to store the last 15 songs and their lyrics (arbitrary limit) so don't have to fetch again if a song is recently replayed

Things I need to add later:
1. ~~Add a script to store the lyrics of recent songs for some time so don't have to fetch lyrics everytime~~
2. Get and display thumbnail image in background
3. Add settings menu
4. ~~Set spawn location at 3/4 of monitor resolution (currently at a fixed pixel value (2500 as I have thicc monitor))~~
5. Rewrite in C++ to solve dependency issues (not going to happen until after A levels)
    1. Replace polling with event when window name changes (no sense having a polling loop and also an event loop) - will likely be more efficient

idk if adding a license is the correct thing to do but i may asw. not like it affects anything

Issues (will only get fixed after A-levels):
1. KeyError gets thrown when playing some songs (so far the examples ive found are 'Doomer' by Tokyo Manaka and 'ON THE WIND' by Tsundere Alley and Jamie Page) - I dont understand why because I thought I accounted for all KeyErrors