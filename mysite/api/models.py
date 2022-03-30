from django.db import models

# Create your models here.
class Artist(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    artist_name = models.CharField(max_length=100, blank=True, default='')
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']