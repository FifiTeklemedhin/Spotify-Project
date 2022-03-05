import spotipy
from spotipy.oauth2 import SpotifyOAuth

'''
import os

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']
'''


scope = "user-read-recently-played"
# authentication, just made a spotipy object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= SPOTIPY_CLIENT_ID, client_secret= SPOTIPY_CLIENT_SECRET, redirect_uri= SPOTIPY_REDIRECT_URI, scope=scope))

# request client's 50 most recent songs and list them out
results = sp.current_user_recently_played()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
