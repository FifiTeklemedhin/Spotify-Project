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

global scope
global sp_obj

# TODO: put this code into login and authorize other users

# currently just manually logs into my account
scope = "user-top-read"

# authentication, just made a spotipy object
sp_obj = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= credentials.SPOTIPY_CLIENT_ID, client_secret= credentials.SPOTIPY_CLIENT_SECRET, redirect_uri= credentials.SPOTIPY_REDIRECT_URI, scope=scope))


@app.route("/")
# @login_required
def index():

   
    # requests client's top tracks and lists them out w/ link
    # can change time_range param to short_term (past 4 weeks) or middle_term (default, past 6 months)
    # ex: results = sp_obj.current_user_top_tracks(time_range= "short_term")
    short_term_data =  sp_obj.current_user_top_tracks(time_range= "short_term")
    medium_term_data = sp_obj.current_user_top_tracks()
    long_term_data = sp_obj.current_user_top_tracks(time_range= "long_term")
    
    # flask passes in track data in format of a grid: as a list of lists, with each list having a dict of 4 tracks in it (refer to helpers.py for more details)

    return render_template("index.html", short_term_tracks = get_track_grid(short_term_data), medium_term_tracks = get_track_grid(medium_term_data), long_term_tracks = get_track_grid(long_term_data)) # don't need to specify that index.html is in templates folder as render_templates automatically assumes its in there


@app.route("/analysis")
#@long_required
def analyze():

    # ex usage: current_user_top_artists(limit=20, offset=0, time_range='medium_term'), "short_term" is default value for time_range param

    short_term_artists = sp_obj.current_user_top_artists(limit=20, offset=0, time_range='medium_term')
    return render_template("analyze.html", short_term_tracks = get_track_grid(short_term_data), medium_term_tracks = get_track_grid(medium_term_data), long_term_tracks = get_track_grid(long_term_data)) # don't need to specify that index.html is in templates folder as render_templates automatically assumes its in there


# TODO
@app.route("/login")
def login():
    return 0


# TODO: guessing game

# TODO: authorize users

# TODO: reccomendations

#   first analyze info about user, then put those analyzations as seeds into reccomendations function


if __name__ == "__main__":
  app.run()

 
 # ask if alright to use, copied from python dev page : https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/

#  def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash("You need to login first")
#             return redirect(url_for('login_page'))

#     return wrap
    