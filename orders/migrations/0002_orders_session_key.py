# Generated by Django 3.1.dev20191227090824 on 2020-04-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='session_key',
            field=models.CharField(default=0, max_length=128),
            preserve_default=False,
        ),
    ]