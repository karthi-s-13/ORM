from django.db import models

# Create your models here.
from django.contrib import admin
class Movie(models.Model):
    
    movie_name=models.CharField(max_length=100)
    genre=models.CharField(max_length=20)
    budget=models.IntegerField()
    ott=models.CharField(max_length=50)
 
class MovieAdmin(admin.ModelAdmin):
    list_display=('movie_name','genre','budget','ott')