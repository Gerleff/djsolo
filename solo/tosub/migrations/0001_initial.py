# Generated by Django 3.0.11 on 2021-01-26 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tosub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=220, verbose_name='Ссылка')),
                ('short', models.CharField(max_length=220, verbose_name='Сокращенное название')),
                ('ch_id', models.IntegerField(verbose_name='Айди канала')),
            ],
        ),
    ]
