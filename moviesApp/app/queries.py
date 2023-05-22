from . import models


# region Movie

def get_movie_from_name(name: str):
    return models.TitleBasics.objects.raw(f'SELECT * FROM title_basics WHERE "primaryTitle" ILIKE %s LIMIT 50', ['%' + name.lower() + '%'])
    # movies = models.TitleBasics.objects.filter(primarytitle__icontains=name)


def get_movie_from_pk(pk: str):
    try:
        return models.TitleBasics.objects.raw(f'SELECT * FROM title_basics WHERE tconst = %s', [pk])[0]
    except:
        raise KeyError()


def get_rating_from_pk(pk: str):
    try:
        return models.TitleRatings.objects.raw(f'SELECT * FROM title_ratings WHERE tconst = %s', [pk])[0]
    except:
        raise KeyError()


def get_principals_from_pk(pk: str):
    return models.TitlePrincipals.objects.raw(f'SELECT * FROM title_principals WHERE tconst = %s', [pk])

# endregion


# region Movie

def get_person_from_name(name: str):
    return models.NameBasics.objects.raw(f'SELECT * FROM name_basics WHERE "primaryName" ILIKE %s LIMIT 50', ['%' + name + '%'])


def get_person_from_pk(pk: str):
    try:
        return models.NameBasics.objects.raw(f'SELECT * FROM name_basics WHERE nconst = %s', [pk])[0]
    except:
        raise KeyError()

# endregion
