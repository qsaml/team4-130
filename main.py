import os
from SpotifyClient import SpotifyClient
# def userProfile():
#     user = input("Enter Spotify Profile: ")
#     url = f'https://api.spotify.com/v1/users/{user}'
#     return url

def run():
    spotifyClient = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'),
                                  os.getenv('SPOTIFY_USER_ID'))
    artist = input("Enter your favorite artist: ")
    tracks = spotifyClient.getTrack(artist)
    track_ids = [track['id'] for track in tracks]
    playlist = input("What name do you want for you playlist? ")
    was_added_to_library = spotifyClient.add_tracks(playlist, track_ids)
    if was_added_to_library:
        for track in tracks:
            print(f"Added {track['name']} to the library")

if __name__ == '__main__':
    # username = userProfile()
    run()