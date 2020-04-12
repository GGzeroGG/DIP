# Generated by Django 3.1.dev20200118190725 on 2020-04-07 10:25

from django.db import migrations, models
import django.db.models.deletion
import poster.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider', models.BooleanField(default=False, verbose_name='Будет ли товар на слайдере?')),
                ('poster', models.ImageField(help_text='700x200px', upload_to=poster.models.poster_img_name, verbose_name='Изоброжение товара')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='prodposter', to='products.Product')),
            ],
        ),
    ]