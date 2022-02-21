from rest_framework import serializers

from .models import Musician, Album, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = (
            'id','musician','album', 'name'
        )
class AlbumSerializer(serializers.ModelSerializer):
    album_songs = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = (
            'id','musician','name', 'release_year','album_songs'
        )
class MusicianSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)
    class Meta:
        model = Musician
        fields = (
            'id','name','country','albums'
        )        