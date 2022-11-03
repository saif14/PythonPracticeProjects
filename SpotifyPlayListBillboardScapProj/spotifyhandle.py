import spotipy
from spotipy.oauth2 import SpotifyOAuth


from dotenv import load_dotenv
import os

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIFY_KEY")
USERNAME = os.getenv("SPOTIFY_PROFILE")
REDIRECT_URI = "http://google.com/"


def returnSpotifyObject():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://google.com/",
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    return sp


class SpotifyHandle:
    def getSpotifyObj(self):
        return returnSpotifyObject()




