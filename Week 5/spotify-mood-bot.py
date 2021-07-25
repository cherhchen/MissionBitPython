""" README.md
Spotify API

How to use

Install the Spotipy library using pip3 install spotipy 
(or pip3 install spotipy --user) if error 13 occurs

Follow these instructions to register an application and get a client ID and client secret: https://developer.spotify.com/documentation/web-api/quick-start

Set up the library like so, using your client ID and client secret from the previous step:

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

credentials = SpotifyClientCredentials(client_id='xx', client_secret='yy')
spotify = spotipy.Spotify(client_credentials_manager=credentials)

Now the possibilities are endless! Check out Spotipy's API reference to view all the available methods, and go through their examples here. Spotify's official documentation will also help you find out what's possible with their API.

Example project

spotify_mood_bot.py: A chatbot that asks you how you're feeling, recommends a few genres of music, then plays a song from the genre you choose.
"""

# MUST RUN 'pip3 install spotipy' BEFORE USE!!!

import random
import re
import webbrowser

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Follow the instructions at https://developer.spotify.com/documentation/web-api/quick-start
# to register an application and get a client ID and client secret
credentials = SpotifyClientCredentials(client_id='8570a7fdbdcf4fa5a99f71fac042d616', client_secret='f5c358f698724421b1e5e4af7324938f')
spotify = spotipy.Spotify(client_credentials_manager=credentials)

mood_regex_to_genres = {
  r'happy|excited|great|fantastic|good|:\)|:D': ['happy', 'party'],
  r'sad|down|depressed|bad|:\(': ['acoustic', 'piano', 'sad'],
  r'stressed': ['classical', 'jazz'],
  r'angry|frustrated|pissed|>:\(': ['heavy-metal', 'hip-hop', 'metal'],
  r'(in )?lov(e|ing|ed)?|<3': ['romantic'],
  r'sleepy|zzz|tired': ['ambient', 'sleep'],
}

def choose_index(options):
  '''Displays a numbered list of `options` to the user and prompts them to select one.'''
  for i, option in enumerate(options, 1):
    print(f'{i}. {option}')
  while True:
    response = input(
      f'Please enter a number from 1 to {len(options)}, or leave blank to let me choose! ')
    if not response:
      return random.randrange(len(options))
    try: index = int(response)
    except: continue
    if index > 0 and index <= len(options):
      return index - 1

def play_song(genre):
  print(f'Searching for a few "{genre}" songs...')
  recommendations = spotify.recommendations(seed_genres=[genre], limit=10)
  # Filter out tracks without Spotify URLs
  tracks = [t for t in recommendations['tracks'] if 'spotify' in t['external_urls']]
  track_titles = [t['artists'][0]['name'] + ' - ' + t['name'] for t in tracks]
  print(f'I found a few "{genre}" songs for you:')
  track = tracks[choose_index(track_titles)]
  print(f'Playing {track["name"]} by {track["artists"][0]["name"]}...')
  webbrowser.open(track['external_urls']['spotify'])

def main():
  response = input('How are you feeling today?\n')
  while True:
    for mood_regex, genres in mood_regex_to_genres.items():
      if re.compile(mood_regex, re.IGNORECASE).search(response):
        print('Which of these genres would you like to listen to?')
        return play_song(genres[choose_index(genres)])
    response = input('Hmm, I could not quite understand that. Can you please reword that?\n')

if __name__ == '__main__':
  main()