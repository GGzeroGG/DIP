# Generated by Django 3.1.dev20200410100027 on 2020-06-10 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0004_productsinorder_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsinorder',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(default='', verbose_name='Комментариий к заказу'),
            preserve_default=False,
        ),
    ]
