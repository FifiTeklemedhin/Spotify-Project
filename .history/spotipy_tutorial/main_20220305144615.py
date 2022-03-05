import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-recently-played"
# authentication, just made a spotipy object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= process.env.SPOTIPY_CLIENT_ID, client_secret= process.env.SPOTIPY_CLIENT_SECRET, redirect_uri= process.env.SPOTIPY_REDIRECT_URI, scope=scope))

# request client's 50 most recent songs and list them out
results = sp.current_user_recently_played()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
