# Generated by Django 4.2 on 2023-05-17 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_games_show_in_slider_alter_review_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='new',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Новинка'),
        ),
    ]