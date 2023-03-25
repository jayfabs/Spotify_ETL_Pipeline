# Dependencies
import spotipy
from openpyxl import Workbook
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np
from pprint import pprint
import json
import datetime

#api_keys
from config import secret
from config import cid

cid = cid
secret = secret

#Connect to API
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

creator = "spotify"
playlist_id = "37i9dQZF1DX4JAvHpjipBk"

playlist = sp.user_playlist_tracks(creator, playlist_id)

#loop through and extract needed data
track_features = []
try:
    

    for track in playlist['items']:
        
        playlist_features = {}

    # Get metadata
        playlist_features['added_date'] = track["track"]["album"]["release_date"]
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["explicit"] = track["track"]["explicit"]
        playlist_features["popularity"] = track["track"]["popularity"]
        playlist_features["track_id"] = track["track"]["id"]
        playlist_features["artist_id"] = track["track"]["album"]["artists"][0]["id"]
        playlist_features["isrc"] = track["track"]["external_ids"]["isrc"]
        
        #Append the playlist_features list to include the data
        track_features.append(playlist_features)
except TypeError:
    pass

#Transform the list into a json file and write it as playlist.json
playlist_json = json.dumps(track_features)

with open("/usr/local/airflow/dags/main_files/playlist.json", "w") as f:
    f.write(playlist_json)

print("main.py ran succesfully!")
