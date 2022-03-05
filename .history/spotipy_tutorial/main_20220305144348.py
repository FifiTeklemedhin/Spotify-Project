import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred 

scope = "user-read-recently-played"
# authentication, just made a spotipy object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))

# request client's 50 most recent songs and list them out
