# Generated by Django 3.1.dev20200410100027 on 2020-06-05 21:51

import catalog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='URL категории')),
                ('img', models.ImageField(upload_to=catalog.models.category_img_name, verbose_name='Картинка категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название компании')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='URL производителя')),
                ('img', models.ImageField(help_text='500x500px', upload_to=catalog.models.manufacture_img_name, verbose_name='Логотип компании')),
                ('country', models.CharField(max_length=60, verbose_name='Страна производитель')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
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
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
                ('manufacture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.manufacture', verbose_name='Производитель')),
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
                ('img', models.ImageField(upload_to=catalog.models.product_img_name)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prodimg', to='catalog.product')),
            ],
            options={
                'verbose_name': 'Картинка товара',
                'verbose_name_plural': 'Картинки товаров',
            },
        ),
    ]
