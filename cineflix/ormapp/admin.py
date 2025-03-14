from django.contrib import admin

# Register your models here.
from .models import Movie,MovieAdmin
admin.site.register(Movie,MovieAdmin)