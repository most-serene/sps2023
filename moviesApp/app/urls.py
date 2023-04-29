from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("movie/<str:tconst>", views.movie_detail, name="detail"),
]
