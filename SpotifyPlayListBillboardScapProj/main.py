from bs4 import BeautifulSoup
import requests
import spotipy
from spotifyhandle import SpotifyHandle

spotifyhandle = SpotifyHandle()

year = input("Input Year: ")
month = input("Input Month: ")
day = input("Input Day: ")

date = year+"-"+month+"-"+day

URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

top_100_songs = soup.select(".o-chart-results-list__item h3")

top_song_list = [song.getText().strip() for song in top_100_songs]
print(top_song_list)

sp = spotifyhandle.getSpotifyObj()
user_id = sp.current_user()["id"]

song_uris = []

for song in top_song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} My Historic Billboard 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)