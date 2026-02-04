# Day 46: Spotify Playlist Creator -- APIs & OAuth Authentication

## What You Learned
You combined web scraping (BeautifulSoup) with API interactions (Spotipy). You learned how to authenticate with OAuth, make API requests, and create resources (playlists) programmatically.

---

## Key Concepts

### 1. OAuth Authentication Flow
OAuth is a secure way to access services without storing passwords:
```python
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        redirect_uri="http://example.com",
        scope="user-library-read",  # Permissions needed
        show_dialog=True,
        cache_path='token.txt'  # Store token locally
    )
)
```

**Why:** OAuth avoids storing passwords. First run opens browser for user consent; token cached for future use. This is industry standard.

### 2. Environment Variables (.env file)
Storing secrets in code is dangerous:
```python
from dotenv import load_dotenv
import os

load_dotenv("../.env")  # Load from .env file
client_id = os.getenv("spotify_client_id")
client_secret = os.getenv("spotify_client_secret")
```

**.env file structure:**
```
spotify_client_id=YOUR_ID
spotify_client_secret=YOUR_SECRET
```

**Why:** .env files keep secrets out of git. Use `git ignore .env` to prevent accidental commits.

### 3. Web Scraping + API Combination
Your project flows like this:
```
1. Scrape Billboard.com for top 100 songs of a specific date
2. For each song, search Spotify API
3. Get song URI from search results
4. Create playlist and add songs to it
```

**Why:** Many real-world projects combine multiple data sources (scrape, then augment with APIs).

### 4. User Input & Date Validation
```python
date_selected = input("Which year you do want to travel to? Enter the date in YYYY-MM-DD format: ")
# Input: "2000-12-01"
year = date_selected.split("-")[0]  # Extract year: "2000"
```

**Why:** User input drives the automation. Parsing dates enables flexible querying.

### 5. Scraping Billboard Charts
```python
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_selected}")
billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, "html.parser")

# Find all song titles
billboard_100_list = soup.select(selector="div li ul li h3")

# Extract text from each h3
songs_list = [song.getText().strip() for song in billboard_100_list]
```

**Why:** CSS selectors target specific structure. `.strip()` removes whitespace. List comprehension is concise.

### 6. Searching Spotify API
```python
result = sp.search(q=f"track:{song} year:{year}", type="track")

try:
    uri = result["tracks"]["items"][0]["uri"]
    spotify_song_uri_list.append(uri)
except IndexError:
    print(f"{song} doesn't exist in Spotify. Skipped.")
```

**Why:** Search query includes year to improve accuracy. IndexError handling prevents crashes when song not found.

### 7. Creating & Managing Playlists
```python
user_id = sp.current_user()["id"]  # Get logged-in user's ID

# Create playlist (returns playlist object)
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date_selected} Billboard 100",
    public=False  # Private playlist
)

# Add songs to playlist
sp.playlist_add_items(
    playlist_id=playlist['id'],
    items=spotify_song_uri_list  # List of song URIs
)
```

**Why:** Playlist creation requires user ID. URIs uniquely identify songs across Spotify. Batch adding is more efficient than adding one-by-one.

### 8. Handling API Errors Gracefully
```python
try:
    uri = result["tracks"]["items"][0]["uri"]
    spotify_song_uri_list.append(uri)
except (IndexError, KeyError):
    print(f"{song} not found on Spotify")
    # Continue with next song instead of crashing
```

**Why:** APIs fail (song not found, network issues, etc.). Defensive coding prevents crashes.

### 9. Token Caching
```python
cache_path='token.txt'  # Spotify saves token here
```

First run: Opens browser for consent → token saved to `token.txt`
Subsequent runs: Reads token from `token.txt` → No browser needed

**Why:** Token caching improves UX. Users don't need to authenticate repeatedly.

### 10. Connecting Concepts
This project is synthesis of previous days:
- **Days 41-44:** Understand HTML structure (Billboard page)
- **Day 45:** Scraping with BeautifulSoup
- **Day 46:** APIs and authentication (Spotify)
- **Days 33-40:** Similar APIs (ISS tracker, weather, stock market)

---

## Common Pitfalls
- **Hardcoding secrets in code**: Store in .env file, add to .gitignore
- **Not handling songs not on Spotify**: Some songs might not exist. Use try/except.
- **Token expiry**: OAuth tokens expire. Spotipy handles refresh automatically.
- **Wrong scope permissions**: Request only scopes you need (`user-library-read`, `playlist-modify-public`, etc.)
- **Not stripping whitespace from scraped text**: Whitespace breaks searches. Use `.strip()`
- **Assuming API response structure**: Different songs might have different response formats. Check existence before accessing.
- **Rate limiting**: Don't hammer APIs. Spotipy handles this, but be mindful in large batches.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 45** | Web scraping Billboard charts |
| **Days 33-40** | API usage patterns (similar to weather, stock APIs) |
| **Day 39-40** | Database/list storage (storing playlist URIs is like storing flight deals) |
| **Day 48** | Selenium automates browser; Spotipy automates API (different automation types) |

---

## Before You Move On

Make sure you can:
- [ ] Understand OAuth flow and why it's better than passwords
- [ ] Use environment variables to store secrets
- [ ] Combine scraping (BeautifulSoup) with API calls
- [ ] Parse API responses and extract needed data
- [ ] Handle IndexError/KeyError when data is missing
- [ ] Create and manage resources via APIs (playlists, etc.)
- [ ] Use token caching to avoid re-authentication
- [ ] Build multi-step automation (scrape → search → create)

---

## Practice Prompt
**Extend the Spotify playlist creator:**

1. **Multiple dates:** Create playlists for dates spanning a year (monthly top 100)
2. **Playlist organization:** Group songs by artist or decade
3. **Statistics:** Print stats (total songs found, not found, artists represented)
4. **Filtering:** Skip songs that don't exist on Spotify vs. use closest match
5. **Error handling:** Log which songs failed and why
6. **Automation:** Schedule script to run weekly and create new playlists

**Challenge:** Scrape from different chart sources (UK charts, other genres) and create comparable playlists for each.
