from django.db import models

# Create your models here.


class Film(models.Model):
    names = models.CharField('Название', max_length=220)
    ugly_name = models.CharField('Название для поиска', max_length=220)
    links = models.URLField("Ссылка", max_length=220)
    kp_rate = models.CharField("КП рейтинг", null=True, max_length=50)
    kp_links = models.URLField("КП ссылка", max_length=220, null=True)
    imdb_rate = models.CharField("ИМДБ рейтинг", null=True, max_length=50)
    imdb_links = models.URLField("ИМДБ ссылка", max_length=220, null=True)
    included = models.BooleanField("Включен в выдачу", default=True)

    class Meta:
        db_table = 'film'


class Serial(models.Model):
    names = models.CharField('Название', max_length=220)
    ugly_name = models.CharField('Название для поиска', max_length=220)
    links = models.URLField("Ссылка", max_length=220)
    kp_rate = models.CharField("КП рейтинг", null=True, max_length=50)
    kp_links = models.URLField("КП ссылка", max_length=220, null=True)
    imdb_rate = models.CharField("ИМДБ рейтинг", null=True, max_length=50)
    imdb_links = models.URLField("ИМДБ ссылка", max_length=220, null=True)
    included = models.BooleanField("Включен в выдачу", default=True)

    class Meta:
        db_table = 'serial'
