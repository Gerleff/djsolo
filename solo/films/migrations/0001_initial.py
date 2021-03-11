# Generated by Django 3.1.6 on 2021-02-04 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=220, verbose_name='Название')),
                ('ugly_name', models.CharField(max_length=220, verbose_name='Название для поиска')),
                ('links', models.URLField(max_length=220, verbose_name='Ссылка')),
                ('kp_rate', models.FloatField(verbose_name='КП рейтинг')),
                ('kp_links', models.URLField(max_length=220, verbose_name='КП ссылка')),
                ('imdb_rate', models.FloatField(verbose_name='ИМДБ рейтинг')),
                ('imdb_links', models.URLField(max_length=220, verbose_name='ИМДБ ссылка')),
                ('included', models.BooleanField(default=True, verbose_name='Включен в выдачу')),
            ],
            options={
                'db_table': 'films_films',
            },
        ),
    ]
