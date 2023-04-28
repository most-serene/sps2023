from django.http import HttpResponse
from django.template import loader

import random

from . import models

def home(request):
    template = loader.get_template("app/index.html")
    movies = []
    if request.method == "GET" and "name" in request.GET.keys():
        subtitle = f'Results for query: "{request.GET["name"]}"'
        movies = models.TitleBasics.objects.filter(primarytitle__icontains= request.GET["name"])
    else:
        subtitle = f'Movies you might be interested in'
        while len(movies) < 9:
            randId = f"tt{''.join([str(random.randint(0,9)) for _ in range(7)])}"
            try:
                movie = models.TitleBasics.objects.get(pk=randId)
                if movie.titletype == "movie":
                    movies.append(movie)
            except:
                pass

    return HttpResponse(template.render({"movies": movies, "subtitle": subtitle}, request))
