"""Subscription related models"""
from django.db import models


class Tosub(models.Model):
    """Sub channel's model"""
    link = models.CharField('Ссылка', max_length=220)
    short = models.CharField("Сокращенное название", max_length=220)
    ch_id = models.CharField("Айди канала", max_length=50)
    
    class Meta:
        """Meta-data"""
        db_table = 'tosub'
