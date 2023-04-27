# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class NameBasics(models.Model):
    nconst = models.TextField(primary_key=True)
    primaryname = models.TextField(db_column='primaryName', blank=True, null=True)  # Field name made lowercase.
    birthyear = models.IntegerField(db_column='birthYear', blank=True, null=True)  # Field name made lowercase.
    deathyear = models.IntegerField(db_column='deathYear', blank=True, null=True)  # Field name made lowercase.
    primaryprofession = models.TextField(db_column='primaryProfession', blank=True, null=True)  # Field name made lowercase.
    knownfortitles = models.TextField(db_column='knownForTitles', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'name_basics'


class TitleAkas(models.Model):
    titleid = models.TextField(db_column='titleId', primary_key=True)  # Field name made lowercase. The composite primary key (titleId, ordering) found, that is not supported. The first column is selected.
    ordering = models.IntegerField()
    title = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    types = models.TextField(blank=True, null=True)
    attributes = models.TextField(blank=True, null=True)
    isoriginaltitle = models.BooleanField(db_column='isOriginalTitle', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'title_akas'
        unique_together = (('titleid', 'ordering'),)


class TitleBasics(models.Model):
    tconst = models.TextField(primary_key=True)
    titletype = models.TextField(db_column='titleType', blank=True, null=True)  # Field name made lowercase.
    primarytitle = models.TextField(db_column='primaryTitle', blank=True, null=True)  # Field name made lowercase.
    originaltitle = models.TextField(db_column='originalTitle', blank=True, null=True)  # Field name made lowercase.
    isadult = models.BooleanField(db_column='isAdult', blank=True, null=True)  # Field name made lowercase.
    startyear = models.IntegerField(db_column='startYear', blank=True, null=True)  # Field name made lowercase.
    endyear = models.IntegerField(db_column='endYear', blank=True, null=True)  # Field name made lowercase.
    runtimeminutes = models.IntegerField(db_column='runtimeMinutes', blank=True, null=True)  # Field name made lowercase.
    genres = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'title_basics'


class TitleCrew(models.Model):
    tconst = models.TextField(primary_key=True)
    directors = models.TextField(blank=True, null=True)
    writers = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'title_crew'


class TitleEpisode(models.Model):
    tconst = models.TextField(primary_key=True)
    parenttconst = models.TextField(db_column='parentTconst', blank=True, null=True)  # Field name made lowercase.
    seasonnumber = models.IntegerField(db_column='seasonNumber', blank=True, null=True)  # Field name made lowercase.
    episodenumber = models.IntegerField(db_column='episodeNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'title_episode'


class TitlePrincipals(models.Model):
    tconst = models.TextField(primary_key=True)  # The composite primary key (tconst, ordering) found, that is not supported. The first column is selected.
    ordering = models.IntegerField()
    nconst = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    characters = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'title_principals'
        unique_together = (('tconst', 'ordering'),)


class TitleRatings(models.Model):
    tconst = models.TextField(primary_key=True)
    averagerating = models.DecimalField(db_column='averageRating', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    numvotes = models.IntegerField(db_column='numVotes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'title_ratings'
