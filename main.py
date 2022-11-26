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
    short_term_data =  sp_obj.current_user_top_tracks(time_range= "short_term") # refer to docs/sample_top_tracks.json for sample output
    medium_term_data = sp_obj.current_user_top_tracks()
    long_term_data = sp_obj.current_user_top_tracks(time_range= "long_term")
    
    # flask passes in track data in format of a grid: as a list of lists, with each list having a dict of 4 tracks in it (refer to helpers.py for more details)

    return render_template("index.html", short_term_tracks = get_track_grid(short_term_data), medium_term_tracks = get_track_grid(medium_term_data), long_term_tracks = get_track_grid(long_term_data)) # don't need to specify that index.html is in templates folder as render_templates automatically assumes its in there


@app.route("/analysis")
#@long_required
def analyze():

    # ex usage: current_user_top_artists(limit=20, offset=0, time_range='medium_term'), "short_term" is default value for time_range param

    short_term_artists = sp_obj.current_user_top_artists(limit=4, offset=0)
    medium_term_artists = sp_obj.current_user_top_artists(limit=4, offset=0, time_range='medium_term') #refer to docs/sample_top_artists.json for sample output
    long_term_artists = sp_obj.current_user_top_artists(limit=4, offset=0, time_range='long_term')
    top_artists = {"short_term": short_term_artists, "medium_term": medium_term_artists, "long_term": long_term_artists}


    
    for idx, artist in enumerate(long_term_artists['items']): 
        print("{}\n\n".format(artist))

    return render_template("analysis.html", top_artists = top_artists) # don't need to specify that index.html is in templates folder as render_templates automatically assumes its in there


# TODO: authorize other users
@app.route("/login")
def login():
    return render_template("login.html")

# TODO: reccomendations
@app.route("/recommendations")
def reccomend():
    return render_template("recommendations.html")

# TODO: guessing game
@app.route("/game")
def guessing_game():
    return render_template("game.html")




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
    