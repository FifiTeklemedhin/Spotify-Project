
from asyncore import write
from email.mime import image
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials
import sys
import math
import random
from collections import Counter

def get_guessing_game_stats(sp_obj, offset):

    short_term_top_artists = get_top_artists(sp_obj, limit = 100, offset = offset, time_range = "short_term")["items"]
    medium_term_top_artists = get_top_artists(sp_obj, limit = 100, offset = offset, time_range = "medium_term")["items"]
    long_term_top_artists = get_top_artists(sp_obj, limit = 100, offset = offset, time_range = "long_term")["items"]

    short_term_top_tracks = sp_obj.current_user_top_tracks(limit = 100, offset=offset, time_range="short_term")["items"]
    medium_term_top_tracks = sp_obj.current_user_top_tracks(limit = 100, offset=offset, time_range="medium_term")["items"]
    long_term_top_tracks = sp_obj.current_user_top_tracks(limit = 100, offset=offset, time_range="long_term")["items"]

    # used this code to find most frequent element in a list: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    short_term_genres = []
    medium_term_genres = []
    long_term_genres = []

    # gets all genres of all artists user listens to for a time range
    for index in range(len(short_term_top_artists)): # all the top artist dictionaries should be the same length
        short_term_genres += short_term_top_artists[index]["genres"]
        medium_term_genres += medium_term_top_artists[index]["genres"]
        long_term_genres += long_term_top_artists[index]["genres"]

    # gets most common genre among artists for each term
    counter = Counter(short_term_genres)
    short_term_top_genre = counter.most_common(1)[0][0]

    counter = Counter(medium_term_genres)
    medium_term_top_genre = counter.most_common(1)[0][0]

    counter = Counter(long_term_genres)
    long_term_top_genre = counter.most_common(1)[0][0]

    print("TOP GENREs: {}, {}, {}".format(short_term_top_genre, medium_term_top_genre, long_term_top_genre))

    # final dictionaries that are returned with data for each term

    top_genres = {"short_term": short_term_top_genre, "medium_term": medium_term_top_genre, "long_term": long_term_top_genre}

    average_popularity_of_artists = {"short_term": get_popularity_stats(short_term_top_artists, "artist")["mean"], "medium_term": get_popularity_stats(medium_term_top_artists, "artist")["mean"], "long_term": get_popularity_stats(long_term_top_artists, "artist")["mean"]}
    average_popularity_of_tracks = {"short_term": get_popularity_stats(short_term_top_tracks, "track")["mean"], "medium_term": get_popularity_stats(medium_term_top_tracks, "track")["mean"], "long_term": get_popularity_stats(long_term_top_tracks, "track")["mean"]}
    
    first_top_artists = {"short_term": short_term_top_artists[0]["name"], "long_term": long_term_top_artists[0]["name"], "medium_term": medium_term_top_artists[0]["name"]}
    first_top_tracks = {"short_term": short_term_top_tracks[0]["name"], "long_term": long_term_top_tracks[0]["name"], "medium_term": medium_term_top_tracks[0]["name"]}

    # returns data for use in main.py

    return {"average_popularity_of_artists": average_popularity_of_artists, 'average_popularity_of_tracks': average_popularity_of_tracks, 'first_top_artists': first_top_artists,'first_top_tracks': first_top_tracks, 'top_genres': top_genres}
   
    
def get_popularity_stats(artists_or_tracks_list, track_or_artist): # requires user to specify if passing in track or artist because the way the popularity is indexed depends on it
    mean = 0
    mode_ranges = {"1-10": 0, "11-20": 0, "21-30": 0, "31-40": 0, "41-50": 0, "51-60":0, "61-70": 0, "71-80":0, "81-90":0, "91-100":0}
    highest_mode_range = "1-10"

    for artist_or_track in artists_or_tracks_list:
        popularity = 0

        if(track_or_artist == "artist"):
            popularity = artist_or_track["popularity"]
        else :
             popularity = artist_or_track["popularity"]

        mean += artist_or_track["popularity"]
        
        for i in range(11, 110, 10):
            if(popularity < i):
                mode_index = "{}-{}".format(i-10, i-1)
                mode_ranges[mode_index] +=1
   
    mean = mean / len(artists_or_tracks_list)  
    for mode_range in mode_ranges:
        # if several modes, selects highest
        if mode_ranges[mode_range] >= mode_ranges[highest_mode_range]:
            highest_mode_range = mode_range # gets the range name (ie "0-20")
    
    return {"mean": mean, "highest_mode_range": highest_mode_range}


def is_artist_or_song_person(num_songs_per_artist): # outputs a string of whether a user is more of an artist or song person depending on the % of artists they only have 1-2 songs they listen to
    count = 0 # counts number of artists that user is only listening 1-2 songs for
    num_artists = len(num_songs_per_artist)

    for num in num_songs_per_artist:
        if num <= 2:
            count +=1
    
    # if user listens to only 1-2 songs for more than 50% of artists, they are a song person
    if (count / num_artists) > .5:
        return "song"
    
    else:
        return "artist"

def term_analysis(sp_obj, limit, offset, time_range, num_associated_artists):
    term_top_artists = get_top_artists(sp_obj, limit = limit, offset = offset, time_range= time_range)
    term_user_top_tracks = sp_obj.current_user_top_tracks(limit = 100, offset = offset, time_range= time_range)

    all_user_top_tracks = [] #used to get popularity stats on tracks
    num_songs_per_artist = []
    artist_data = {}

    for artist in term_top_artists["items"]:
        user_top_tracks = [] # get the tracks of the artist that the user is currently listening to most
        for track_index in range(len(term_user_top_tracks["items"])):
            track_id = term_user_top_tracks["items"][track_index]["album"]['artists'][0]["id"]
            if track_id == artist["id"]:
                user_top_tracks.append(term_user_top_tracks["items"][track_index])
                all_user_top_tracks.append(term_user_top_tracks["items"][track_index])

        # a limited number of artist's top tracks in US; artist_top_tracks() has no limit param
        num_top_tracks = num_associated_artists if num_associated_artists <= 5 else 5 # want the same number of tracks as associated artists for more uniform formatting, or up to 5
        limited_artist_top_tracks = sp_obj.artist_top_tracks(artist["id"], country="US")["tracks"][0:num_top_tracks] 

        # gets a small number of associated artists to list on page. artist_related_artists() doesn't have a limit field
        associated_artists = sp_obj.artist_related_artists(artist["id"])["artists"]
        limited_associated_artists = [associated_artists[random.randint(0, len(associated_artists)-1)] for i in range(num_associated_artists)]
        
        # artist or song person
        num_songs_per_artist.append(len(user_top_tracks))

        artist_data[artist["name"]] = {"user_top_tracks": user_top_tracks, "artist_top_tracks": limited_artist_top_tracks, "associated_artists": limited_associated_artists}

    return {"top_artists": term_top_artists, "artist_data": artist_data, "artist_or_song_person": is_artist_or_song_person(num_songs_per_artist), "artist_popularity_stats": get_popularity_stats(term_top_artists["items"], "artist"), "track_popularity_stats": get_popularity_stats(all_user_top_tracks, "track")}
        
def get_recs_from_random_danceability(sp_obj, limit, offset):
     # gets total of 5 seeds (max allowed by spotify): two top artists and two top tracks over the past few months, and 1 random genre
    top_artists = sp_obj.current_user_top_artists(limit = 2, offset=offset, time_range="medium_term")
    top_artist_ids = [artist["id"] for artist in top_artists["items"]] # gets ids of artists

    top_tracks = sp_obj.current_user_top_tracks(limit = 2, offset=offset, time_range="medium_term")
    top_track_ids = [track["id"] for track in top_tracks["items"]] # gets ids of tracks
    
    genres = sp_obj.recommendation_genre_seeds()["genres"]
    random_genre = [genres[random.randint(0, len(genres) - 1)]] #1 random genre from the available genres, must be passed in as an list

    return sp_obj.recommendations(limit = limit, seed_artists = top_artist_ids, seed_tracks = top_track_ids, seed_genres = random_genre, danceability= random.randint(0,1))

def get_recs_from_tracks(sp_obj, limit, offset):
    # gets maximum number of top artists (100) for increased randomness
    short_term_top_tracks = sp_obj.current_user_top_tracks(limit = 100, offset=offset, time_range="short_term")
    medium_term_top_tracks = sp_obj.current_user_top_tracks(limit = 100, offset=offset, time_range="medium_term")
    long_term_top_tracks = sp_obj.current_user_top_tracks(limit = 100, offset=offset, time_range="long_term")

    num_tracks = len(short_term_top_tracks)

    # selects a random short, medium, and long term track to be part of the seed tracks, medium tracks get 3 spots since users probably enjoy the tracks but aren't sick of them
    random_tracks = [short_term_top_tracks["items"][random.randint(0,  num_tracks-1)]["id"], medium_term_top_tracks["items"][random.randint(0, num_tracks - 1)]["id"] , medium_term_top_tracks["items"][random.randint(0, num_tracks - 1)]["id"], long_term_top_tracks["items"][random.randint(0, num_tracks - 1)]["id"], long_term_top_tracks["items"][random.randint(0, num_tracks - 1)]["id"]]
    
    return sp_obj.recommendations(seed_tracks= random_tracks, limit=limit)

def get_recs_from_random_genres(sp_obj, limit):
    genres = sp_obj.recommendation_genre_seeds()["genres"]
    random_genres = [genres[random.randint(0, len(genres) - 1)] for i in range(5)] # creates a list of 5 random genres from the available genres. 5 seed values is max
    return sp_obj.recommendations(seed_genres=random_genres, limit=limit)

def get_recs_from_artists(sp_obj, limit, offset):

    # gets max number of artists for increased randomness
    short_term_top_artists = get_top_artists(sp_obj, limit = 100, offset = offset, time_range = "short_term")
    medium_term_top_artists = get_top_artists(sp_obj, limit = 100, offset = offset, time_range = "medium_term")
    long_term_top_artists = get_top_artists(sp_obj, limit = 100, offset = offset, time_range = "long_term")

    num_artists = len(short_term_top_artists)

    # selects a random short, medium, and long term artist to be part of the seed artists
    random_artists = [short_term_top_artists["items"][random.randint(0,  num_artists-1)]["id"],  medium_term_top_artists["items"][random.randint(0, num_artists - 1)]["id"], medium_term_top_artists["items"][random.randint(0, num_artists - 1)]["id"]]
    return sp_obj.recommendations(seed_artists= random_artists, limit= limit)


def get_top_artists(sp_obj, limit, offset, time_range):

    return sp_obj.current_user_top_artists(limit= limit, offset= offset, time_range= time_range)

def get_track_grid(results):

     # to create track grid, hands html track data as a list of lists, with each list having a dict of 4 tracks in it

    '''
    ex: 
    [
        [{track_data}, {track_data}, {track_data}, {track_data}],
        [{track_data}, {track_data}, {track_data}, {track_data}],
        [{track_data}, {track_data}, {track_data}, {track_data}],
        [{track_data}, {track_data}, {track_data}, {track_data}]
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

    return track_data