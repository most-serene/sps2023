from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
import time
from . import models
from . import queries


def home(request):
    file = open("./times.csv", "a")
    template = loader.get_template("app/index.html")
    movies = []
    subtitle = "Search a movie"
    if request.method == "GET" and "name" in request.GET.keys():
        subtitle = f'Results for query: "{request.GET["name"]}"'
        start = time.time()
        movies = queries.get_movie_from_name(request.GET["name"])

    response = HttpResponse(template.render({"movies": movies, "subtitle": subtitle}, request))
    if request.method == "GET" and "name" in request.GET.keys():
        end = time.time()
        file.write(f"name,{end-start}\n")
        file.close()
    return response


def movie_detail(request, tconst):
    file = open("./times.csv", "a")
    template = loader.get_template("app/movieDetail.html")
    try:
        start = time.time()
        movie = queries.get_movie_from_pk(tconst)
        rating = queries.get_rating_from_pk(tconst)
        principals = queries.get_principals_from_pk(tconst)
        actor_names = {queries.get_person_from_pk(person.nconst): person for person in principals if person.category in ['actor', 'actress']}
        cast_names = {queries.get_person_from_pk(person.nconst): person for person in principals if person.category not in ['actor', 'actress']}
    except:
        print("Error")
        return redirect(home)


    response = HttpResponse(template.render({
        "movie": movie,
        "rating": rating,
        "actors": actor_names.items(),
        "cast": cast_names.items(),
    }, request))

    end = time.time()
    file.write(f"id,{end - start}\n")
    file.close()
    return response
