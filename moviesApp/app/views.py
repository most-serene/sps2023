from django.http import HttpResponse
from django.template import loader

import random

from . import models

def home(request):
    template = loader.get_template("app/index.html")
    actors = []
    if request.method == "GET" and "name" in request.GET.keys():
        subtitle = f'Results for query: "{request.GET["name"]}"'
        actors = models.NameBasics.objects.filter(primaryname__icontains= request.GET["name"])
    else:
        subtitle = f'People you might be interested in'
        while len(actors) < 9:
            randId = f"nm{''.join([str(random.randint(0,9)) for _ in range(7)])}"
            try:
                actors.append(models.NameBasics.objects.get(pk=randId))
            except:
                pass

    return HttpResponse(template.render({"actors": actors, "subtitle": subtitle}, request))
