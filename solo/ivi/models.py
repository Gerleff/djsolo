from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


class Ivi(models.Model):
    name = models.CharField(max_length=220)
    year = models.CharField(max_length=10)
    description = models.TextField()
    synopsis = models.TextField()
    admitad_link = models.URLField()
    poster_url = models.URLField()
    ivi_rate = models.FloatField()
    kp_rate = models.CharField(max_length=10)
    imdb_rate = models.CharField(max_length=10)
    ivi_id = models.IntegerField()
    kp_id = models.IntegerField()
    genres = ArrayField(models.IntegerField(blank=True, null=True))
    categories = ArrayField(models.IntegerField(blank=True, null=True))

    class Meta:
        abstract = True


class Film(Ivi):
    class Meta:
        db_table = 'ivi_film'


class Serial(Ivi):
    class Meta:
        db_table = 'ivi_serial'
