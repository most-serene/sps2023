from django.http import HttpResponse
from django.template import loader

from . import models

def index(request):
    template = loader.get_template("app/index.html")
    actors = models.NameBasics.objects.all()[:20]
    print(actors)
    return HttpResponse(template.render({"actors": actors}, request))