# Generated by Django 2.1.5 on 2021-05-13 10:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likesnew', to=settings.AUTH_USER_MODEL),
        ),
    ]
