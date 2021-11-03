import os
from SpotifyClient import SpotifyClient
# def userProfile():
#     user = input("Enter Spotify Profile: ")
#     url = f'https://api.spotify.com/v1/users/{user}'
#     return url

def run():
    spotifyClient = SpotifyClient("BQAdiJ23_PY5yfPvS2AXq3Xm5jEOm17ClKjb4k9kGHEsIRbqAUTLkGZ8_p1HThpWafoAhPb03v3WEbE8abIRpYgK4P6UxziTz1eZpJ4JNkVboyQc5M2TqUtsFUyyVToRkIztAoJHi_iMQG83LI82Yyx9CmRmfX1P54POmSIupVULdUJ",
                                  "BQCaXQgsRBbaqx9nfvGeZr80hJW3G3LJ8k")
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