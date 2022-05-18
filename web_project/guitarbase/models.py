from django.db import models

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=120)

    def __str__(self):
        return self.artist_name

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=360)
    capo = models.IntegerField()
    tuning = models.CharField(max_length=120)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.song_name

class Verse(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    verse_chord_prog = models.CharField(max_length=360, blank=True)

class Chorus(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    chorus_chord_prog = models.CharField(max_length=360, blank=True)

    class Meta:
        verbose_name_plural = 'Choruses'

class Bridge(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    bridge_chord_prog = models.CharField(max_length=360, blank=True)
    
