from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        managed = True


class Artist(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        managed = True


class Song(models.Model):
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True, blank=True)
    colabs = models.ManyToManyField('Artist', related_name='colabs')
    genres = models.ManyToManyField('Genre')
    title = models.CharField(null=False, blank=False, max_length=200)
    duration = models.PositiveIntegerField(null=False, blank=False, default=1)
    url = models.URLField(null=True, blank=True, max_length=250)
    songfile = models.FileField(null=False, blank=False, upload_to=settings.CMP_STORAGE)
    likes = models.PositiveIntegerField(null=False, blank=False, default=0)
    dilikes = models.PositiveIntegerField(null=False, blank=False, default=0)

    class Meta:
        managed = True


class Playlist(models.Model):
    songs = models.ManyToManyField('Song')
    name = models.CharField(null=False, blank=False, max_length=200)

    class Meta:
        managed = True
