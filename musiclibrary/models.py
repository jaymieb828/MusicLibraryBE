from datetime import date
from itertools import product
from re import M
from sqlite3 import Date
from django.db import models
from django.forms import CharField, DateField
from pytz import timezone



# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=255)
