# Generated by Django 3.1.6 on 2021-03-26 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210314_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(editable=False, null=True, verbose_name='Контент')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'mailing',
            },
        ),
        migrations.CreateModel(
            name='MailMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.IntegerField()),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.mailing', verbose_name='Рассылка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Пользователь')),
            ],
            options={
                'db_table': 'mail_message',
            },
        ),
        migrations.AddField(
            model_name='mailing',
            name='users',
            field=models.ManyToManyField(through='users.MailMessage', to='users.User'),
        ),
    ]
