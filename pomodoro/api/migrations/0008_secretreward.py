# Generated by Django 3.2.8 on 2021-10-30 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_delete_redeemedrewards'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecretReward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_contet', models.TextField()),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reward')),
            ],
        ),
    ]
