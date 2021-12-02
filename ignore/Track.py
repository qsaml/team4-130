class Track:
    def __init__(self, name, id, artist):
        self.name = name
        self.id = id
        self.artist = artist

    def spotify_Uri(self):
        return f"spotify:track:{self.id}"

    def __str__(self):
        return self.name + "by" + self.artist