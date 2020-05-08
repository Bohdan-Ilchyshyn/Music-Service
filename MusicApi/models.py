from django.db import models

GENRE = (
    ("Unknown", "Unknown"),
    ("Movie", "Movie"),
    ("Pop", "Pop"),
    ("Rock", "Rock"),
    ("Alternative/Indie", "Alternative/Indie"),
    ("Remix", "Remix"),
    ("Instrumental", "Instrumental"),
    ("Folk", "Folk"),
    ("Electronic", "Electronic")
)


class Artist(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.first_name + '' + self.last_name


class Album(models.Model):
    name = models.CharField(max_length=45, null=False)
    genre = models.CharField(max_length=200, choices=GENRE, default=GENRE[0][0])
    cover = models.ImageField(upload_to='media/covers/')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=45, null=False)
    file = models.FileField(upload_to='media/musics/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=45, null=False)
    cover = models.ImageField(upload_to='media/covers/')
    playlist = models.ForeignKey(Music, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name
