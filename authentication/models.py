from django.contrib.auth.models import AbstractUser
from django.db import models
from django.apps import apps

# Playlist = apps.get_model('MusicApi', 'Playlist')

class User(AbstractUser):
    pl = models.ForeignKey('MusicApi.Playlist', on_delete=models.DO_NOTHING, null=True, blank=True)