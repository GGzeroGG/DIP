# Generated by Django 3.1.dev20191227090824 on 2020-04-11 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orders_price_per_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='quantity',
            new_name='quantity_nbr',
        ),
    ]