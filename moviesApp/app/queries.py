from . import models

# region Movie


def get_movie_from_name(name: str):
    movies = models.TitleBasics.objects.raw(f'SELECT * FROM title_basics WHERE LOWER("primaryTitle") LIKE %s', ['%' + name + '%'])
    # movies = models.TitleBasics.objects.filter(primarytitle__icontains=name)
    return movies


def get_movie_from_pk(pk: str):
    try:
        return models.TitleBasics.objects.raw(f'SELECT * FROM title_basics WHERE tconst = %s', [pk])[0]
    except:
        raise KeyError()

# endregion
