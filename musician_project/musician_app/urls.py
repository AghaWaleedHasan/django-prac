from rest_framework import routers
from .views import AlbumViewSet, MusicianViewSet, SongViewSet
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'musicians', MusicianViewSet)
router.register(r'albums',AlbumViewSet)
router.register(r'songs',SongViewSet)
urlpatterns = [
    path('admin/',admin.site.urls), 
    path('',include(router.urls))
]