from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Director(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 64, unique = True)

class Star(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 64, unique = True)

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 64, unique = True)

    
class Film(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    year = models.CharField(max_length=12)
    runtime = models.CharField(max_length=12)
    rating = models.CharField(max_length=12)
    genres = models.ManyToManyField(Genre, blank=True, related_name="films")
    image = models.URLField()
    description = models.CharField(max_length=500)
    directors = models.ManyToManyField(Director, blank=True, related_name = "films")
    stars = models.ManyToManyField(Star, blank=True, related_name="films")

    def json(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "year" : self.year,
            "runtime" : self.runtime,
            "rating" : self.rating,
            "genres" : [genre.name for genre in self.genres.all()],
            "image" : self.image,
            "description" : self.description,
            "directors" : [director.name for director in self.directors.all()],
            "stars" : [star.name for star in self.stars.all()],
            "users" : [user.username for user in list(self.users.all())],
            "watchers" : [user.username for user in list(self.watchers.all())]
        }


class User(AbstractUser):
    watchlist = models.ManyToManyField(Film, blank=True, related_name="users")
    watchedlist = models.ManyToManyField(Film, blank=True, related_name="watchers")