import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials

'''
import os

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']
'''

scope = "user-top-read"
# authentication, just made a spotipy object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= credentials.SPOTIPY_CLIENT_ID, client_secret= credentials.SPOTIPY_CLIENT_SECRET, redirect_uri= credentials.SPOTIPY_REDIRECT_URI, scope=scope))


# requests client's top tracks and lists them out
results = sp.current_user_top_tracks()

print(enumaerate(results['items']['artists']))

'''
for idx, track in enumerate(results['items']):
    print(idx, track['artists'][0]['name'], " – ", track['name'])
'''



'''
# request client's 50 most recent songs and list them out
results = sp.current_user_recently_played()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

'''


