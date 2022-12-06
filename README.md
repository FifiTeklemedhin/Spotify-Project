# Spotify-Project
An app that creates wrap (recap of top songs, artists, minutes listened every month, perhaps with new recommendations) each month. Integrates a goal system with this wrapped; ie how much I have listened v how much I want to each month

# Tutorials
* Used [this link](https://developer.spotify.com/documentation/web-api/quick-start/) to create a serverside app that can access user related data (commit 1). No actual functionality of my independent app yet, template and basic connections to user are done though!!
# Navigation
## Web-api-auth-examples -> authorization_code
### public (folder)
* stores all webpages user will see

### app.js
* main code fo the app

# Authorization
Used [this extension](https://github.com/vanortg/Flask-Spotify-Auth) to access the log-in client for spotify. I do not have a strong enough understanding of Flask and Python or JavaScript to access the client more manually. Learning to do so with the limited documentation I found online would have been a project in and of itself. I verified with a TF that I could use this extension so long as I cite it.