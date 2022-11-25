from asyncore import write
from email.mime import image
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials
import sys
import math

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

    
    # creating a list of lists, with each list having a dict of 4 tracks in it

    '''
    ex: 
    [
        [{}, {}, {}, {}],
        [{}, {}, {}, {}],
        [{}, {}, {}, {}],
        [{}, {}, {}, {}]
    ]
    '''
    new_line = ""
    col_count = 1
    row_count = 1
    track_data = []
    current_row = []

    
    num_tracks = len(list(enumerate(results['items']))) 
    num_cols = 4 #number of tracks per row
    num_rows = math.ceil(num_tracks / num_cols) 
    remainder_cols = num_tracks % num_rows #remaining tracks if there is a row of uneven tracks



    for idx, track in enumerate(results['items']): # from what I understand, need index as a placeholder for key ( enums are key-value pairs), track as value
        track_name = track['artists'][0]['name'] + " – " + track['name']
        track_link = track['external_urls']['spotify'] # used as unique identifier
        image_link = track['album']['images'][0]["url"]
        artist_name = track['artists'][0]['name'] # I think it currently only gets one artist name even if there are many

        # inserts data into track
        current_track = dict()
        current_track = {"track_name": track_name, "track_link": track_link, "artist_name" : artist_name, "image_link": image_link}
        current_row.append(current_track)

        if col_count == num_cols:
            track_data.append(current_row)
            current_row = []
            col_count = 1
            row_count +=1

        elif num_rows == row_count and col_count == remainder_cols: # if on the last row and the last track, append row to list
            track_data.append(current_row)
            break
        else:
            col_count+=1

    # flask passes data to html pages
    return render_template("index.html", track_data = track_data) # don't need to specify that index.html is in templates folder as render_templates automatically assumes its in there



if __name__ == "__main__":
  app.run()

 
    