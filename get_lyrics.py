import requests

def search_keys(data) -> int:
    for k, v in data.items():
        if k == "message" or k == "":
            return 0
        elif k == "lyrics":
            return 1
    return 2

def remove_spaces(name: str) -> str:
    temp_list = name.split(" ")
    x = ""
    i = 0

    for i in temp_list:
        x += i
    
    return x
    
def get_lyrics(song: str, artist: str) -> str:
    if artist == "Spotify" or artist == "Spotify Free" or artist == "Spotify Premium":
        lyrics = "No song is currently playing"

    else:
        #Tries Youtube
        URL = f"https://lyrics.lewdhutao.my.eu.org/v2/youtube/lyrics?title={song}&artist={artist}"
        # print(URL)
        response_code = requests.get(URL)
        # print(response_code)
        x = response_code.json()
        # print(x)
        data = response_code.json()["data"]
        # print(data)

        check_data = search_keys(data)

        if check_data == 0:
            # URL = f"https://lyrics.lewdhutao.my.eu.org/v2/musixmatch/lyrics?title={song}&artist={artist}"
            # # print(URL)
            # response_code = requests.get(URL)
            # # x = response_code.json()
            # # print(x)
            # data = response_code.json()["data"]

            # check_data = search_keys(data)
            # if check_data == 0:
            #     lyrics = f"The lyrics for {song} by {artist} were not found"
            # elif check_data == 1:
            #     lyrics = data["lyrics"]
            # elif check_data == 2:
            #     lyrics = "i dont know went wrong"
            lyrics = f"The lyrics for {song} by {artist} were not found"
        elif check_data == 1:
            lyrics = data["lyrics"]
        elif check_data == 2:
            lyrics = "someting went wrong beep beep oh no"
    
    # print(lyrics)
    return lyrics

#~~# TEST IT #~~#
# from get_song_artist import song, artist
# get_lyrics(song, artist)