# Generated by Django 3.1.6 on 2021-03-14 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrPages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField()),
            ],
            options={
                'db_table': 'err_pages',
            },
        ),
        migrations.CreateModel(
            name='ErrPagesSer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField()),
            ],
            options={
                'db_table': 'err_pages_ser',
            },
        ),
        migrations.CreateModel(
            name='LastLoadedFilm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('date', models.CharField(max_length=220)),
            ],
            options={
                'db_table': 'last_loaded_film',
            },
        ),
        migrations.CreateModel(
            name='LastLoadedSerial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('date', models.CharField(max_length=220)),
            ],
            options={
                'db_table': 'last_loaded_serial',
            },
        ),
    ]
