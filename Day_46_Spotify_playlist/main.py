import os
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# PATTERN: Load environment variables from .env file (never hardcode secrets!)
# .env contains spotify_client_id and spotify_client_secret
load_dotenv("../.env")
spotify_client_id = os.getenv("spotify_client_id")
spotify_client_secret = os.getenv("spotify_client_secret")

# INPUT: Get date from user (drives which Billboard chart to scrape)
date_selected = input("Which year you do want to travel to? Enter the date in YYYY-MM-DD format: ")

# SCRAPING: Fetch Billboard Hot 100 chart for the specified date
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_selected}")
billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, "html.parser")

# SCRAPING: CSS selector targets song title h3 elements
# Structure: div > li > ul > li > h3 (specific to Billboard page structure)
billboard_100_list = soup.select(selector="div li ul li h3")

# PATTERN: List comprehension to extract and clean text from each title
# .strip() removes leading/trailing whitespace (important for search accuracy)
songs_list = [song.getText().strip() for song in billboard_100_list]

# print(songs_list)  # Debug: view extracted song titles

# AUTHENTICATION: OAuth flow for Spotify
# First run: Opens browser for user consent → token saved to 'token.txt'
# Subsequent runs: Reads cached token from 'token.txt' → No browser needed
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=spotify_client_id,
    client_secret=spotify_client_secret,
    redirect_uri="http://example.com",
    scope="user-library-read",  # Permissions: read user library
    show_dialog=True,  # Force re-login if needed
    cache_path='token.txt'  # Cache token locally
))

# PATTERN: Collect song URIs to add to playlist
spotify_song_uri_list = []

# LOGIC: Extract year from date (e.g., "2000-12-01" → "2000")
year = date_selected.split("-")[0]

# AUTHENTICATION: Get current user's ID (needed for playlist creation)
user_id = sp.current_user()["id"]

# PATTERN: Loop through Billboard songs, search Spotify, collect URIs
for song in songs_list:
    # API SEARCH: Query Spotify for track matching song title and year
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        # PATTERN: Extract first search result's URI (unique Spotify identifier)
        uri = result["tracks"]["items"][0]["uri"]
        spotify_song_uri_list.append(uri)
    except IndexError:
        # ERROR HANDLING: Song not found on Spotify (happens often)
        print(f"{song} doesn't exist in Spotify. Skipped.")
        # Continue to next song instead of crashing

print(spotify_song_uri_list)  # Debug: view collected URIs

# API: Create new private playlist
# Returns playlist object containing id, name, etc.
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date_selected} Billboard 100",
    public=False  # Private playlist (not visible to others)
)
print(playlist)

# API: Add all collected songs to the newly created playlist
# Batch operation is more efficient than adding songs one-by-one
sp.playlist_add_items(playlist_id=playlist['id'], items=spotify_song_uri_list)
