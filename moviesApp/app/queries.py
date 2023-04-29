from . import models
def get_movie_from_name(name):
    movies = models.TitleBasics.objects.raw(f"SELECT * FROM title_basics WHERE LOWER(\"primaryTitle\") LIKE '%%{name}%%'")
    # movies = models.TitleBasics.objects.filter(primarytitle__icontains=name)
    return movies

def get_movie_from_pk(pk):
    try:
        movie = models.TitleBasics.objects.raw(f"SELECT * FROM title_basics WHERE tconst = '{pk}'")[0]
    except:
        raise FileNotFoundError()
    return movie