from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = models.Playlist.objects.all()
    serializer_class = serializers.PlaylistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer


class BandViewSet(viewsets.ModelViewSet):
    queryset = models.Band.objects.all()
    serializer_class = serializers.BandSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = models.Music.objects.all()
    serializer_class = serializers.MusicSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer
