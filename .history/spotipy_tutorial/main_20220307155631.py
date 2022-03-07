from asyncore import write
from email.mime import image
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials
import sys

def writeTopTracksHTML():   
    # literally just makes a file
    f = open('helloworld.html','w')

    message = """<html>
    <head></head>
    <body>
    <p>Hello World!</p>
    {}
    </body>
    </html>"""

    link_song_placeholder = "<a href=\"{}\">{}</a><br/></br>"
    image_placeholder = "<img width=\"250px\" src=\"{}\" alt=\"{}\">"
    scope = "user-top-read"

    # authentication, just made a spotipy object
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= credentials.SPOTIPY_CLIENT_ID, client_secret= credentials.SPOTIPY_CLIENT_SECRET, redirect_uri= credentials.SPOTIPY_REDIRECT_URI, scope=scope))

    # requests client's top tracks and lists them out w/ link
    # can change time_range to short_term (past 4 weeks) or middle_term (default, past 6 months)
    results = sp.current_user_top_tracks(time_range= "long_term")

    ##print(results['items'][0]['name'] + " : " + results['items'][0]['external_urls']['spotify'])
    new_line = ""
    for idx, track in enumerate(results['items']):
        song_name = track['artists'][0]['name'] + " – " + track['name']
        link = track['external_urls']['spotify']
        image_link = track['album']['images'][0]["url"]
        print(image_link)

        new_line += image_placeholder.format(image_link, song_name) + "\n" + link_song_placeholder.format(link, song_name)
    f.write(message.format(new_line))
    f.close()



writeTopTracksHTML()
#print(results['items'][0]['album']['images'][0]["url"])

