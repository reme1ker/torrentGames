# Generated by Django 4.2 on 2023-05-21 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_remove_cart_total_price_order_payed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='game',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
