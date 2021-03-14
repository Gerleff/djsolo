from django.db import models


class LastLoadedFilm(models.Model):
    name = models.CharField(max_length=220)
    date = models.CharField(max_length=220)

    class Meta:
        db_table = 'last_loaded_film'


class LastLoadedSerial(models.Model):
    name = models.CharField(max_length=220)
    date = models.CharField(max_length=220)

    class Meta:
        db_table = 'last_loaded_serial'


class ErrPages(models.Model):
    page = models.IntegerField()

    class Meta:
        db_table = 'err_pages'


class ErrPagesSer(models.Model):
    page = models.IntegerField()

    class Meta:
        db_table = 'err_pages_ser'
