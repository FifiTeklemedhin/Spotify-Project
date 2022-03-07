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
        image_link = results['items'][0]['album']['images'][0]["url"]

        new_line += link_song_placeholder.format(link, song_name) + "\n" + image_placeholder.format(image_link, song_name)

    f.write(message.format(new_line))
    f.close()



scope = "user-top-read"
str = ""
# authentication, just made a spotipy object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= credentials.SPOTIPY_CLIENT_ID, client_secret= credentials.SPOTIPY_CLIENT_SECRET, redirect_uri= credentials.SPOTIPY_REDIRECT_URI, scope=scope))

# requests client's top tracks and lists them out w/ link
# can change time_range to short_term (past 4 weeks) or middle_term (default, past 6 months)
results = sp.current_user_top_tracks(time_range= "long_term")

print(results['items'][0]['album']['images'][0]["url"])

'''
for idx, track in enumerate(results['items']):
    str += (idx, track['artists'][0]['name'], " – ", track['name'], "\n" , track['external_urls']['spotify'], "\n")
'''





'''
{'album': 
    {'album_type': 'SINGLE', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/1W7FNibLa0O0b572tB2w7t'},
     'href': 'https://api.spotify.com/v1/artists/1W7FNibLa0O0b572tB2w7t', 
     'id': '1W7FNibLa0O0b572tB2w7t', 'name': 'Pink Sweat$', 'type': 'artist', 
     'uri': 'spotify:artist:1W7FNibLa0O0b572tB2w7t'}], 'available_markets': [], 
     'external_urls': {'spotify': 'https://open.spotify.com/album/3TTHQTyBu7n3f48pwBtMDu'}, 
     'href': 'https://api.spotify.com/v1/albums/3TTHQTyBu7n3f48pwBtMDu', 'id': '3TTHQTyBu7n3f48pwBtMDu', 
     'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2739bacb25620556225574a7392', 'width': 640}
'''

