from . import models
def get_movie_from_name(name):
    movies = models.TitleBasics.objects.raw(f"SELECT * FROM title_basics as tb WHERE LOWER(\"primaryTitle\") LIKE '%%{name}%%'")
    # movies = models.TitleBasics.objects.filter(primarytitle__icontains=name)
    return movies