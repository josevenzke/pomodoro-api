# Generated by Django 3.2.8 on 2021-10-29 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211029_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pomodorotree',
            old_name='current_pomodors',
            new_name='all_time_pomodoros',
        ),
        migrations.AddField(
            model_name='pomodorotree',
            name='current_pomodoros',
            field=models.IntegerField(default=0),
        ),
    ]
