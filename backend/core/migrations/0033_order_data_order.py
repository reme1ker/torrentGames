# Generated by Django 4.2 on 2023-05-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='data_order',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
