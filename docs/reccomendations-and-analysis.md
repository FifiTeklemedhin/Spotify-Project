 # Goal
 first analyze info about user, then put those analyzations as seeds into reccomendations function
 generate reccs for each time period (according to short term, medium term, long term)

## Analysis
- analyze following info
    - [] artists: pass in id
    - [] genre
    - [] tracks
    - [] danceability
        * could do 1 standard deviation from avg danceability for min/max danceability params

- actually can't analyze tracks and danceability
- artists: 
    - can do short-middle-long term
    - try maybe comparing num hours a user listens to a specific artist v average min usrs listen to them for
    - try maybe listing their top artists and their most popular songs v the songs the user listens tp
         - get_artist top tracks
    - popularity, genres of each artist
        - get_artist
    - related artists
        - https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artists-related-artists
- top genres: iterate 
   

