from asyncore import write
from email.mime import image
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials
import sys
from helpers import *
import random

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
    short_term_data =  sp_obj.current_user_top_tracks(limit = 8, time_range= "short_term") # refer to docs/sample_top_tracks.json for sample output
    medium_term_data = sp_obj.current_user_top_tracks(limit = 8)
    long_term_data = sp_obj.current_user_top_tracks(limit = 8, time_range= "long_term")
    
    # flask passes in track data in format of a grid: as a list of lists, with each list having a dict of 4 tracks in it (refer to helpers.py for more details)

    return render_template("index.html", short_term_tracks = get_track_grid(short_term_data), medium_term_tracks = get_track_grid(medium_term_data), long_term_tracks = get_track_grid(long_term_data)) # don't need to specify that index.html is in templates folder as render_templates automatically assumes its in there


@app.route("/analysis", methods=["POST"])
#@long_required
def analyze():
    limit = 4
    offset = 0
    num_associated_artists = 4
    if request.form.get('short_term') == 'short term':
        short_term_analysis = term_analysis(sp_obj, limit, offset, time_range="short_term", num_associated_artists=num_associated_artists) # code in helpers.py
        return render_template("analysis.html", top_artists = short_term_analysis["top_artists"], term = "s h o r t  t e r m", artist_data=short_term_analysis["artist_data"])

    if request.form.get('medium_term') == 'medium term':
       medium_term_analysis = term_analysis(sp_obj, limit, offset, time_range="medium_term", num_associated_artists=num_associated_artists) # code in helpers.py
       return render_template("analysis.html", top_artists = medium_term_analysis["top_artists"], term = "m e d i u m  t e r m", artist_data=medium_term_analysis["artist_data"])

    else:
       long_term_analysis = term_analysis(sp_obj, limit, offset, time_range="long_term", num_associated_artists=num_associated_artists) # code in helpers.py
       return render_template("analysis.html", top_artists = long_term_analysis["top_artists"], term = "l o n g  t e r m", artist_data=long_term_analysis["artist_data"])

    # top_artists = {"short_term": get_top_artists(sp_obj, limit = limit, offset = offset, time_range = "short_term"), "medium_term": get_top_artists(sp_obj, limit = limit, offset = offset, time_range = "medium_term"), "long_term": get_top_artists(sp_obj, limit = limit, offset = offset, time_range = "long_term")}
    # return render_template("analysis.html", top_artists = top_artists) # don't need to specify that index.html is in templates folder as render_templates automatically assumes its in there


# TODO: authorize other users
@app.route("/login")
def login():
    return render_template("login.html")

# TODO: reccomendations
@app.route("/recommendations", methods=["GET", "POST"])
def recommend():

    if request.method == "POST":
        limit = 4
        offset = 0
        recomendations = {}

        if request.form.get('top_artists') == 'Top artists':
            recommendations = get_recs_from_artists(sp_obj, limit=limit, offset=offset)
            return render_template("recommendations.html", recommendations = recommendations)

        if request.form.get('top_tracks') == 'Top tracks':
            recommendations = get_recs_from_tracks(sp_obj, limit, offset)
            return render_template("recommendations.html", recommendations = recommendations)
 
        if request.form.get('random_genres') == 'Random genres':
            recommendations = get_recs_from_random_genres(sp_obj, limit)
            return render_template("recommendations.html", recommendations = recommendations)

        if request.form.get('random_danceability') == 'Random danceability':
           recommendations = get_recs_from_random_danceability(sp_obj, limit, offset)
           return render_template("recommendations.html", recommendations = recommendations)

        # returns empty dict if form is somehow submitted without a button clicked
        return render_template("recommendations.html", recommendations = recomendations)

    else:
        limit = 4
        offset = 0

        short_term_top_artists = get_top_artists(sp_obj, limit = limit, offset = offset, time_range = "short_term")
        medium_term_top_artists = get_top_artists(sp_obj, limit = limit, offset = offset, time_range = "medium_term")
        long_term_top_artists = get_top_artists(sp_obj, limit = limit, offset = offset, time_range = "long_term")

    
        random_artists = [short_term_top_artists["items"][random.randint(0, limit - 1)]["id"],  medium_term_top_artists["items"][random.randint(0, limit - 1)]["id"], medium_term_top_artists["items"][random.randint(0, limit - 1)]["id"]]
    
        recommendations = sp_obj.recommendations(seed_artists= random_artists, limit= limit)


        return render_template("recommendations.html", recommendations = recommendations)

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
    