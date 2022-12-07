# Setup Instructions

Thank you for taking the time to look at my final project! I developed a web app that uses the Spotify API to analyze my listening data. Below are the steps to trying this code out for yourself.


## Navigate to Correct Directory
&nbsp;
- The first step is to open up the command line and `cd` into the directory `project/SPOTIFY-PROJECT CS`. This is the folder where my project implementation (and this document) is located.
    > Note: I'll refer to this path as the `root` for the rest of this walkthrough

- Type `ls` and make sure all of the files and directories below are included:
    ``` powershell
    fifiteklemedhin@Fifis-MacBook-Air Spotify-Project CS % ls     

    README.MD               credentials.py          get-pip.py              implementation_notes.md issues.md               main.py                 pyvenv.cfg              templates
    bin                     docs                    helpers.py              include                 lib                     md_images               static
    fifiteklemedhin@Fifis-MacBook-Air Spotify-Project CS % 
    ```

&nbsp;

## Run Main.py
&nbsp;
- `main.py` is where I have written my Flask code. It is the file that includes is called from the terminal to start the application.
- In the terminal, call `python3 main.py` while in the `root` directory 
    You should receive an output like this in the terminal:
    ``` powershell
    fifiteklemedhin@Fifis-MacBook-Air Spotify-Project CS % python3 main.py

    * Serving Flask app 'main'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://localhost:5002
    Press CTRL+C to quit
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 126-669-324
    ```

    > Note: the port value for this app is `5002` since some versions of MacOS [block API calls](https://stackoverflow.com/questions/69818376/localhost5000-unavailable-in-macos-v12-monterey?noredirect=1&lq=1) for `5000` since it is being used by the system for an AirPlay feature . I worked with a TF to change the port number.

- copy the link `http://localhost:5002" or (CMD+Click on it in the terminal) to navigate to the website. Your browser should open up this webpage:

   ![](/md_images/readme_images/TODO.png)

&nbsp;
&nbsp;
## Common Issues:
these errors can be found at the bottom of the error page that pops up on the site OR in the same terminal page you ran `main.py` in

&nbsp;
### 'requests.exceptions.ConnectionError:
Something similar to: 
``` powershell
raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='api.spotify.com', port=443): Max retries exceeded with url: /v1/me/top/artists?time_range=short_term&limit=4&offset=0 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x106b8e6a0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))
```
- This error simply means you are not connected to a secure wifi network. Connect to a personal hotspot or a password-protected network such as `Harvard Secure`. Stay away from public, passwordless networks like `Harvard University`

&nbsp;
### Internal Server Error:
Something similar to:
``` powershell
The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.
```
- this means that the port you are connected has more processes than it can handle. The port we are using will likely be unused by other applications, so we can ***manually stop*** unnecessary processes running in the background


#### stopping the port:
- find processes by running ```sudo lsof -i:5002``` in `root`
- you will be prompted for the password to your device (PC/Laptop)
    - the password will not show as you're typing, simply press enter when finished
- you will should an output like this:
    ``` powershell
    fifiteklemedhin@Fifis-MacBook-Air Spotify-Project CS % sudo lsof -i:5002
    Password:
    COMMAND   PID            USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
    Python  74685 fifiteklemedhin    4u  IPv4 0x7f34135b211578bb      0t0  TCP localhost:rfe (LISTEN)
    Python  74685 fifiteklemedhin    7u  IPv4 0x7f34135b211578bb      0t0  TCP localhost:rfe (LISTEN)
    Python  74686 fifiteklemedhin    4u  IPv4 0x7f34135b211578bb      0t0  TCP localhost:rfe (LISTEN)
    Python  74686 fifiteklemedhin    7u  IPv4 0x7f34135b211578bb      0t0  TCP localhost:rfe (LISTEN)
    ```
- type ```kill <PID>``` (you find PID from last command) and press enter
- repeat until all ```sudo lsof -i:5002``` returns no PIDs



&nbsp;
### Error: no commands supplied

- if you are getting this error message after running `python3 main.py`, call `python3 main.py build` and press the link to the website that pops up.
- if this doesn't work, call `python3 main.py install` and click on the link again
- if still having trouble, refer to this [forum response](https://stackoverflow.com/questions/19672690/error-no-commands-supplied-when-trying-to-install-pyglet) by `Burham Khalid` 

    > Note: I completely referenced this fix from the forum response above. I just also wrote the likely commands down here for ease of acess.

&nbsp;
### Command not found: "python3"
- check to see if you are using a different version of `python` by typing ```python --version`` into `root`. 
    If an error pops up, try following using different versions of `python`:
    ``` powershell
    python<version> main.py
    ```
- if the command above does not work, refer to [this site](https://www.python.org/downloads/) and to download `python3` manually **into `root`**

&nbsp;
# Using the App
It's finally time to use the app! Below is a quick walkthrough of each page and how to interact with it.

## Home: 
Home is an informational page with details on what my project does, why I chose to develop it, and more. 

## Prediction Game:
A quick trivia form before the user gets into the analysis. 
    - Enter number and words into each mini quiz and press `submit`  to guess the user's listening habits. 
    - The input fields will turn green or red depending on whether you are correct or not.

## Track History:
Navigate to this page and it will display the user's top songs in the short, middle, and long term (of all time). 

## Recommendations
This page generates song recommendations based from random genres or danceability levels, top artists or tracks. 
Click on a button to get random songs. If you refresh the page, the recommendations will automatically regenerate with recommendations based on the top artists.

## Analysis
More complex analysis of artists to balance out `Track History` page. Click on links to navigate to an artist or song. Note that some green text is simply bolded