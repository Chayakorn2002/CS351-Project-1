class Song :
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist

    def __str__(self):
        return f"{self.name} : {self.artist}"