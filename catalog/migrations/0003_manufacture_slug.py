# Generated by Django 3.1.dev20200118190725 on 2020-02-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200226_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacture',
            name='slug',
            field=models.SlugField(default=1, max_length=30, unique=True, verbose_name='понятный url'),
            preserve_default=False,
        ),
    ]