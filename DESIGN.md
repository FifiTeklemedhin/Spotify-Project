# Design Document

## Overview
My project is a simpler version of `Spotify Wrapped`. It will use the Spotify API to analyze a user's music over recent and less recent time periods, and then for all time. It will perhaps offer a quiz at the beginning  and some recommendations at the end.

### Why this App

I love listening to various types of music! I wanted to make an app where I could view my listening data for a ***very** long time, but didn't know where to begin. `JavaScript`, which I found quite difficult to parse, was too intimidating. When I discovered `Flask`, I still had no idea `Jinja` existed.

My CS50 final felt like the opporunity to attempt this app!

### Goals
You can find the outcomes at the end of this document or in README.md

- Good Outcomes: 
    - Analyzing my own spotify data with pages on listening history in recent and longer time spans, then also all time. 

- Better Outcomes: 
    - Allowing for users to authorize the site to use their spotify data or perhaps pass it in as a file. 
    - Creating a guessing game based off of their listening histories.


- Best Outcome:
    - Having a recommendation feature for songs/artists 
    - Creating a (decently) aesthetically pleasing interface.

## Implementation: Data
### 'Short', 'Medium', and 'Long Term'
Spotify returns data for user activity with 3 time ranges:
- Short term:

## Implementation: Technology
### Flask
- I have very little experience with web development. Using `Python` and `Jinja` instead helped me focus on the actual functionality of the app rather than learning a foreign language.
- My main `Flask` app is called `main.py` each function, which has several funtions that render `Jinja` templates with user data


### Spotipy
- I used the [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/#) API, which is a Python wrapper for the regular [Spotify]https://developer.spotify.com/documentation/web-api/) API, to get user data. It has all the functionality of the regular API.
- almost all of my functions, both in `main.py` and `helpers.py` use `Spotipy`

### HTML, CSS,Bootstrap
### Structuring API data
- I am **extremely** proud of my final designs for my website. They not only required SO much time and research, but also required me to structure my data to work best with `Bootstrap`
- Example: Getting a user's track history
    - I wanted to display each track's name and artist in a grid. This required formatting the data in 







## Outcomes:
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

