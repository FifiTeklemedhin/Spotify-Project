
import math

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