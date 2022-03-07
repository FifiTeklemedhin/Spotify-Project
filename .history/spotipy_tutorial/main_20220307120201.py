import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials
import sys


f = open('helloworld.html','w')

message = """<html>
<head></head>
<body>
<p>Hello World!</p>
<p>{}</p>
</body>
</html>"""

#f.write(message)
#f.close()

scope = "user-top-read"

# authentication, just made a spotipy object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= credentials.SPOTIPY_CLIENT_ID, client_secret= credentials.SPOTIPY_CLIENT_SECRET, redirect_uri= credentials.SPOTIPY_REDIRECT_URI, scope=scope))

# requests client's top tracks and lists them out w/ link
# can change time_range to short_term (past 4 weeks) or middle_term (default, past 6 months)
results = sp.current_user_top_tracks(time_range= "long_term")

##print(results['items'][0]['name'] + " : " + results['items'][0]['external_urls']['spotify'])
new_line = ""
for idx, track in enumerate(results['items']):
    new_line += "{}{}{}{}{}{}{}".format(idx, track['artists'][0]['name'], " – ", track['name'], "\n" , track['external_urls']['spotify'], "\n")

f.write(message.format(new_line))
f.close()




'''
def getTopTracks():
    scope = "user-top-read"
    str = ""
    # authentication, just made a spotipy object
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= credentials.SPOTIPY_CLIENT_ID, client_secret= credentials.SPOTIPY_CLIENT_SECRET, redirect_uri= credentials.SPOTIPY_REDIRECT_URI, scope=scope))

    # requests client's top tracks and lists them out w/ link
    # can change time_range to short_term (past 4 weeks) or middle_term (default, past 6 months)
    results = sp.current_user_top_tracks(time_range= "long_term")

    ##print(results['items'][0]['name'] + " : " + results['items'][0]['external_urls']['spotify'])
    for idx, track in enumerate(results['items']):
        str += (idx, track['artists'][0]['name'], " – ", track['name'], "\n" , track['external_urls']['spotify'], "\n")

    return str
'''
