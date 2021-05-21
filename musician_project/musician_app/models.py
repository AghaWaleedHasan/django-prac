from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Musician(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=150)

    def __str__(self):
        return(self.name)

class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=CASCADE, related_name='albums')
    name = models.CharField(max_length=200)
    release_year = models.CharField(max_length=4)

    def __str__(self):
        return(self.name)

class Song(models.Model):
    musician = models.ForeignKey(Musician, on_delete=CASCADE)
    album = models.ForeignKey(Album, on_delete = CASCADE, related_name='album_songs')
    name = models.CharField(max_length=200)

    def __str__(self):
        return(self.name)