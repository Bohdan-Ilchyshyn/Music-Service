from rest_framework import serializers
from . import models


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Music
        fields = ('name', 'album')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        fields = ('name', 'artists', 'band', 'genre', 'cover', 'single', 'description')


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artist
        fields = ('nick_name', 'photo', 'first_name', 'last_name', 'history', 'album_artist')


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Playlist
        fields = ('name', 'cover', 'musics')


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Band
        fields = ('name', 'cover', 'album_band')
