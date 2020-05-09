from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaylistViewSet, AlbumViewSet, ArtistViewSet, MusicViewSet


router = DefaultRouter()
router.register('playlists', PlaylistViewSet)
router.register('artists', ArtistViewSet)
router.register('musics', MusicViewSet)
router.register('albums', AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
]