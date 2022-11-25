from asyncore import write
from email.mime import image
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials
import sys
from helpers import *


from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session
app = Flask(__name__)

@app.route("/")
def index():

    scope = "user-top-read"

    # authentication, just made a spotipy object
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= credentials.SPOTIPY_CLIENT_ID, client_secret= credentials.SPOTIPY_CLIENT_SECRET, redirect_uri= credentials.SPOTIPY_REDIRECT_URI, scope=scope))

    # requests client's top tracks and lists them out w/ link
    # can change time_range param to short_term (past 4 weeks) or middle_term (default, past 6 months)
    # ex: results = sp.current_user_top_tracks(time_range= "short_term")
    results = sp.current_user_top_tracks(time_range= "short_term")
    
    # flask passes in track data in format of a grid: as a list of lists, with each list having a dict of 4 tracks in it (refer to helpers.py for more details)

    return render_template("index.html", track_data = get_track_grid(results)) # don't need to specify that index.html is in templates folder as render_templates automatically assumes its in there



if __name__ == "__main__":
  app.run()

 
    