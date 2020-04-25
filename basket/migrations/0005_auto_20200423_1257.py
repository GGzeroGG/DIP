# Generated by Django 3.1.dev20200410100027 on 2020-04-23 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basket', '0004_auto_20200423_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsinbasket',
            name='order',
        ),
        migrations.RemoveField(
            model_name='productsinbasket',
            name='username_basket',
        ),
        migrations.AddField(
            model_name='productsinbasket',
            name='username',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]