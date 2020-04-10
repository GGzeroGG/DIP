# Generated by Django 3.1.dev20200118190725 on 2020-04-05 19:53

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0002_auto_20200405_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя товара')),
                ('slug', models.SlugField(blank=True, max_length=30, unique=True, verbose_name='URL товара')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добовления')),
                ('price', models.IntegerField(help_text='руб.', verbose_name='Цена')),
                ('warehouse', models.IntegerField(help_text='шт.', verbose_name='Количество товара на складе')),
                ('warranty', models.IntegerField(help_text='месяцев', verbose_name='Гарантия')),
                ('description', models.TextField(verbose_name='Описание')),
                ('specifications', models.TextField(verbose_name='Характеристики')),
                ('set', models.TextField(verbose_name='Комплект поставки')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=products.models.product_img_name)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prodimg', to='products.Product')),
            ],
            options={
                'verbose_name': 'Картинка товара',
                'verbose_name_plural': 'Картинки товаров',
            },
        ),
    ]
