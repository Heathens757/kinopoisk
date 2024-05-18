from django.shortcuts import render
from .models import *
# main
def main(request):
    movies = Movie.objects.all()
    return render(request, 'kinopoisk/main.html', {
        'movies': movies,
        'title': 'Фильмы',
        })


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'kinopoisk/movies_list.html', {'movies': movies})

def actor_list(request):
    actors = MoviePerson.objects.filter(role = MoviePerson.RoleType.ACTOR)
    return render(request, 'kinopoisk/actors_list.html', {
        'persons': actors, 'title': 'Актёры'
    })

def director_list(request):
    directors = MoviePerson.objects.filter(role = MoviePerson.RoleType.DIRECTOR)
    return render(request, 'kinopoisk/directors_list.html', {
        'persons': directors, 'title': 'Режиссёры'
    })
def sound_engineer_list(request):
    sound_engineers = MoviePerson.objects.filter(role = MoviePerson.RoleType.SOUND_ENGINEER)
    return render(request, 'kinopoisk/sound_engineers_list.html', {
        'persons': sound_engineers, 'title': 'Звукорежиссёры'
    })

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'kinopoisk/genre_list.html', {
        'genres': genres, 'title': 'жанры'
    })


#dinamic
def movie_detail(request, movie_id):
    movie = Movie.objects.get(id = movie_id)
    return render(request, 'kinopoisk/movie_detail.html', {'movie': movie})

def genre_detail(request, genre_id):
    genre = Movie.objects.get(id = genre_id)
    movies = Movie.objects.all()
    return render(request, 'kinopoisk/genre_detail.html', {
        'genre': genre, 'movies': movies
    })

def actor_detail(request, actor_id):
    actor = Movie.objects.get(id = actor_id)
    movies = actor.acted_in_movies.all()
    return render(request, 'kinopoisk/actor_detail.html', {
        'person': actor, 'movies': movies
    })

def director_detail(request, director_id):
    director = Movie.objects.get(id = director_id)
    movies = director.directed_movies.all()
    return render(request, 'kinopoisk/director_detail.html', {
        'person': director, 'movies': movies
    })

def sound_engineer_detail(request, sound_engineer_id):
    sound_engineer = Movie.objects.get(id = sound_engineer_id)
    movies = sound_engineer.sounded_movies.all()
    return render(request, 'kinopoisk/sound_engineer_detail.html', {
        'person': sound_engineer, 'movies': movies
    })