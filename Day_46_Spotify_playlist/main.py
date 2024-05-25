import os
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv("../.env")
spotify_client_id = os.getenv("spotify_client_id")
spotify_client_secret = os.getenv("spotify_client_secret")

date_selected = input("Which year you do want to travel to? Enter the date in YYYY-MM-DD format: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_selected}")
billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, "html.parser")

billboard_100_list = soup.select(selector="div li ul li h3")

songs_list = [song.getText().strip() for song in billboard_100_list]

# print(songs_list)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                               client_secret=spotify_client_secret,
                                               redirect_uri="http://example.com",
                                               scope="user-library-read",
                                               show_dialog=True,
                                               cache_path='token.txt'))


spotify_song_uri_list = []
year = date_selected.split("-")[0]
user_id = sp.current_user()["id"]

for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        spotify_song_uri_list.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(spotify_song_uri_list)

playlist = sp.user_playlist_create(user=user_id, name=f"{date_selected} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist['id'], items=spotify_song_uri_list)
