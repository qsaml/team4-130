from Track import Track
from Playlist import Playlist
import random
import string
import requests
import urllib
import json


class SpotifyClient(object):
    def __init__(self, api_key, user_id):
        self.api_key = api_key
        self.user_id = user_id

    def getTrack(self, artist):
        # wildcard = f'%{artist}%'
        # query = urllib.parse.quote(wildcard)
        # offset = random.randint(0, 2000)
        url = f'https://api.spotify.com/v1/artists/{artist}/top-tracks'
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
        )
        response_json = response.json()
        tracks = [Track(track["name"], track["id"], track["artists"][0]["name"]) for
                  track in response_json["tracks"]]
        print(f'Found {len(tracks)} from your search')
        return tracks

    def add_tracks(self, playlist, tracks):
        track_uri = [track.spotify_Uri() for track in tracks]
        data = json.dumps(track_uri)
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
        response = self.post_API_request(url, data)
        Json_response = response.json()
        return Json_response

    def create_playlist(self, name):
        data = json.dumps({
            "name": name,
            "description": "Songs",
            "public": True
        })
        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = self.post_API_request(url, data)
        JSON_response = response.json()

        playlist_id = JSON_response["id"]
        playlist = Playlist(name, playlist_id)
        return playlist


    def post_API_request(self, url, data):
        response = requests.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
        )
        return response