# Generated by Django 3.1.6 on 2021-04-04 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210327_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='delivered',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mailing',
            name='undelivered',
            field=models.IntegerField(default=0),
        ),
    ]
