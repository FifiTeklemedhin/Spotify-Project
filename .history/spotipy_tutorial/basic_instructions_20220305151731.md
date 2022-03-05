# Basic things to remember (spotipy and generally)
## Venv
### First Steps
* seeing if you have installed it: virtualenv venv
* installing it: python3 -m pip3 install --user virtualenv
* activating: source venv/bin/activate
* deactivating: deactivate

### ENV Variables
* so far have client ID, secret, and redirect URI

## Spotify Info
* uses (scopes)[https://developer.spotify.com/documentation/general/guides/authorization/scopes/], make users know that third party apps only access info they choose to be shared

## killing a port
* find process by doing sudo lsof -i:portNumber
* kill PID (you find PID from last command)
* check to see if port closed (nothing returns in that case)

## ignoring a file
* touch .gitignore in main repo
* add the file name to the .gitignore file
* use this documentation to figure it out
  
### if you accidentally commit a file and want to remove it from staging area
* git rm --cached <file>
* commit changes again