from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

import random

from . import models
from . import queries

def home(request):
    template = loader.get_template("app/index.html")
    movies = []
    subtitle = "Search a movie"
    if request.method == "GET" and "name" in request.GET.keys():
        subtitle = f'Results for query: "{request.GET["name"]}"'
        movies = queries.get_movie_from_name(request.GET["name"])

    return HttpResponse(template.render({"movies": movies, "subtitle": subtitle}, request))


def movie_detail(request, tconst):
    template = loader.get_template("app/movieDetail.html")
    try:
        movie = queries.get_movie_from_pk(tconst)
    except:
        print("Error")
        return redirect(home)
    return HttpResponse(template.render({"movie": movie}, request))
