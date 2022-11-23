from asyncore import write
from email.mime import image
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials
import sys

from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session
app = Flask(__name__)

@app.route("/")
def index():

    message = """<html>
    <head></head>
    <body>
    <p>Hello World!</p>
    {}
    </body>
    </html>"""

    link_song_placeholder = "<a href=\"{}\">{}</a><br/></br>"
    image_placeholder = "<img width=\"250px\" src=\"{}\" alt=\"{}\"><br/></br>"
    scope = "user-top-read"

    # authentication, just made a spotipy object
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= credentials.SPOTIPY_CLIENT_ID, client_secret= credentials.SPOTIPY_CLIENT_SECRET, redirect_uri= credentials.SPOTIPY_REDIRECT_URI, scope=scope))

    # requests client's top tracks and lists them out w/ link
    # can change time_range param to short_term (past 4 weeks) or middle_term (default, past 6 months)
    # ex: results = sp.current_user_top_tracks(time_range= "short_term")
    results = sp.current_user_top_tracks(time_range= "short_term")

    ##print(results['items'][0]['name'] + " : " + results['items'][0]['external_urls']['spotify'])
    
    new_line = ""
    all_track_data = dict()
    for idx, track in enumerate(results['items']): # from what I understand, need index as a placeholder for key ( enums are key-value pairs), track as value
        track_name = track['artists'][0]['name'] + " – " + track['name']
        track_link = track['external_urls']['spotify'] # used as unique identifier
        image_link = track['album']['images'][0]["url"]
        artist_name = track['artists'][0]['name'] # I think it currently only gets one artist name even if there are many

        # inserts data into track
        all_track_data[track_link] = {"track_name": track_name, "artist_name" : artist_name, "image_link": image_link}
    print(all_track_data)
    
    return render_template("index.html", all_track_data = all_track_data) # don't need to specify that index.html is in templates folder as render_templates automatically assumes its in there



if __name__ == "__main__":
  app.run()

 
    