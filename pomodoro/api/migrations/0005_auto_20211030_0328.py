# Generated by Django 3.2.8 on 2021-10-30 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_create_at_pomodoro_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pomodoro',
            old_name='pomodotree',
            new_name='pomodorotree',
        ),
        migrations.DeleteModel(
            name='TimeSpent',
        ),
    ]
