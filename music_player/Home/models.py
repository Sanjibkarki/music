from django.db import models

# Create your models here.
class Music(models.Model):
    singer_name = models.CharField(max_length=100)
    singer_image = models.FileField(upload_to='image/')

    def __str__(self):
        return self.singer_name
class Album(models.Model):
    singer  = models.ForeignKey(Music, on_delete=models.CASCADE)
    song_name = models.CharField(max_length = 200)
    songs = models.FileField(upload_to ='playlist/')
    favourites = models.BooleanField(default = False)
    