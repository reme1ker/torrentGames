# Generated by Django 4.2 on 2023-05-19 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_games_new'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='movie',
            new_name='game',
        ),
    ]
