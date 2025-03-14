# Ex02 Django ORM Web Application
## Date: 11.03.2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin

# Register your models here.
from .models import Movie,MovieAdmin
admin.site.register(Movie,MovieAdmin)

models.py

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
```


## OUTPUT
![alt text](<Screenshot 2025-03-14 083550.png>)


## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
