# Generated by Django 3.1.6 on 2021-03-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20210311_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='ivi_description',
            field=models.TextField(null=True, verbose_name='Описание от IVI'),
        ),
        migrations.AddField(
            model_name='film',
            name='ivi_link',
            field=models.URLField(max_length=220, null=True, verbose_name='Ссылка IVI'),
        ),
        migrations.AddField(
            model_name='serial',
            name='ivi_description',
            field=models.TextField(null=True, verbose_name='Описание от IVI'),
        ),
        migrations.AddField(
            model_name='serial',
            name='ivi_link',
            field=models.URLField(max_length=220, null=True, verbose_name='Ссылка IVI'),
        ),
        migrations.AlterField(
            model_name='film',
            name='kp_links',
            field=models.URLField(max_length=220, null=True, unique=True, verbose_name='КП ссылка'),
        ),
        migrations.AlterField(
            model_name='serial',
            name='kp_links',
            field=models.URLField(max_length=220, null=True, unique=True, verbose_name='КП ссылка'),
        ),
    ]