from bs4 import BeautifulSoup
import requests as r
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import os

SPOTIPY_CLIENT_KEY = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']

date = input("To when would you like to go? (YYYY-MM-DD)")
billboard_url = f'https://billboard.com/charts/hot-100/{date}'

billboard_response = r.get(billboard_url)
billboard_html = billboard_response.text

billboard_soup = BeautifulSoup(billboard_html, 'html.parser')

first_artist_class = "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet"
artists_class = "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"

first_artist = billboard_soup.find_all(name='span', class_=first_artist_class)
artists = billboard_soup.find_all(name='span', class_=artists_class)
artists.insert(0, first_artist[0])

artist_names = []
for artist in artists:
    filtered_artist_name = artist.getText().replace('\n', '')
    artist_names.append(filtered_artist_name)

first_song_class = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet"
songs_class = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"

first_song = billboard_soup.find_all(name='h3', class_=first_song_class)
tracks = billboard_soup.find_all(name='h3', class_=songs_class)
tracks.insert(0, first_song[0])

# get tracks and put track,artist tuples to a list
song_names = []
for track in tracks:
    filtered_song_name = track.getText().replace('\n', '')
    song_names.append(filtered_song_name)

top100 = list(zip(artist_names, song_names))

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


# get track URIs and put to a list
track_uris = []
for track in top100:
    query = f"{track[1]},{track[0]}"
    result = sp.search(query, limit=1)
    if len(result['tracks']['items']) > 0:
        uri = result['tracks']['items'][0]['uri']
        track_uris.append(uri)


scope = "playlist-modify-public"
sp2 = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_KEY,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=scope))

user_id = sp2.me()['id']

playlist = f'{date}-Playlist'
playlist_data = sp.user_playlist_create(user_id, playlist)
playlist_id = playlist_data['id']

sp2.playlist_add_items(playlist_id, track_uris)

