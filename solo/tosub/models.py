from django.db import models


class Tosub(models.Model):
    link = models.CharField('Ссылка', max_length=220)
    short = models.CharField("Сокращенное название", max_length=220)
    ch_id = models.CharField("Айди канала", max_length=50)
