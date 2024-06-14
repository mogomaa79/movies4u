from final.models import *
import json

def main(File):
    with open(File, "r") as file:
        data = json.load(file)
        
    setGenres = set()
    setStars = set()
    setDirectors = set()

    for film in data:
        genres = film['genre'].split(', ')
        for genre in genres:
            setGenres.add(genre)

    for film in data :
        stars = film['stars']
        for star in stars :
            setStars.add(star)
            
    for film in data:
        setDirectors.add(film['director'])
        
    for star in setStars:
        x = Star(name = star)
        x.save()
        
    for genre in setGenres:
        x = Genre(name = genre)
        x.save()

    for director in setDirectors:
        x = Director(name = director)
        x.save()
        
    for film in data:
        stars = film['stars']
        genres = film['genre'].split(', ')
        x = Film(id = film['id'], name = film['name'], year = film['year'], runtime = film['runtime'], image = film['image'], description = film['description'], rating = film['rating'])
        x.save()
        for star in stars:
            x.stars.add(Star.objects.filter(name=star).first())
        for genre in genres:
            x.genres.add(Genre.objects.filter(name=genre).first()) 
            x.directors.add(Director.objects.filter(name=film['director']).first())

if __name__ == '__main__':
    main("films.json")