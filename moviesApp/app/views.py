from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from . import models
from . import queries
from django.db import connection

def home(request):
    file = open("./times.csv", "a")
    template = loader.get_template("app/index.html")
    movies = []
    subtitle = "Search a movie"
    if request.method == "GET" and "name" in request.GET.keys():
        subtitle = f'Results for query: "{request.GET["name"]}"'
        movies = list(queries.get_movie_from_name(request.GET["name"]))

    file.write(f"name,{float(connection.queries[0]['time'])}\n")
    file.close()

    return HttpResponse(template.render({"movies": movies, "subtitle": subtitle}, request))


def movie_detail(request, tconst):
    file = open("./times.csv", "a")
    template = loader.get_template("app/movieDetail.html")
    try:
        movie = queries.get_movie_from_pk(tconst)
        rating = queries.get_rating_from_pk(tconst)
        principals = queries.get_principals_from_pk(tconst)
        actor_names = {queries.get_person_from_pk(person.nconst): person for person in principals if person.category in ['actor', 'actress']}
        cast_names = {queries.get_person_from_pk(person.nconst): person for person in principals if person.category not in ['actor', 'actress']}
    except:
        print("Error")
        return redirect(home)


    tot_time = sum([float(q["time"]) for q in connection.queries])
    file.write(f"id,{tot_time}\n")
    file.close()

    return HttpResponse(template.render({
        "movie": movie,
        "rating": rating,
        "actors": actor_names.items(),
        "cast": cast_names.items(),
    }, request))
