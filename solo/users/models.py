from django.db import models


class User(models.Model):
    name = models.CharField('Логин', max_length=220)
    user_id = models.IntegerField("Телеграм айди")



