class Playlist:
    def __init__(self, pid, name, style, description):
        self.pid = pid
        self.name = name
        self.style = style
        self.description = description
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        song_output = "\n".join(str(song) for song in self.songs)
        return f"Playlist ID: {self.pid}\nName: {self.name}\nStyle: {self.style}\nDescription: {self.description}\nSongs:\n{song_output}"