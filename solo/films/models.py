from django.db import models


# Create your models here.

class Films(models.Model):
    names = models.CharField('Название', max_length=220)
    ugly_name = models.CharField('Название для поиска', max_length=220)
    links = models.URLField("Ссылка", max_length=220)
    kp_rate = models.FloatField("КП рейтинг")
    kp_links = models.URLField("КП ссылка", max_length=220)
    imdb_rate = models.FloatField("ИМДБ рейтинг")
    imdb_links = models.URLField("ИМДБ ссылка", max_length=220)
    included = models.BooleanField("Включен в выдачу", default=True)

    class Meta:
        db_table = 'films_films'
# class UglyNames(models.Model):
#     names = models.ForeignKey()
