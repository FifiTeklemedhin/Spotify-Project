
from asyncore import write
from email.mime import image
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials
import sys
import math
import random

def get_recs_from_random_genres(sp_obj, limit):
    genres = sp_obj.recommendation_genre_seeds()["genres"]
    random_genres = [genres[random.randint(0, len(genres) - 1)] for i in range(5)] # creates a list of 5 random genres from the available genres. 5 seed values is max
    return sp_obj.recommendations(seed_genres=random_genres, limit=limit)

def get_recs_from_artists(sp_obj, limit, offset):
    short_term_top_artists = get_top_artists(sp_obj, limit = limit, offset = offset, time_range = "short_term")
    medium_term_top_artists = get_top_artists(sp_obj, limit = limit, offset = offset, time_range = "medium_term")
    long_term_top_artists = get_top_artists(sp_obj, limit = limit, offset = offset, time_range = "long_term")

    # selects a random short, medium, and long term artist to be part of the seed artists
    random_artists = [short_term_top_artists["items"][random.randint(0, limit - 1)]["id"],  medium_term_top_artists["items"][random.randint(0, limit - 1)]["id"], medium_term_top_artists["items"][random.randint(0, limit - 1)]["id"]]
        
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