# Generated by Django 2.1.5 on 2021-05-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_category',
            field=models.CharField(choices=[('Yapay Zeka', 'Yapay Zeka'), ('Yazılım', 'Yazılım'), ('Kripto Para', 'Kripto Para'), ('Donanım', 'Donanım')], default='Yazılım', max_length=20, verbose_name='Makale Kategori'),
        ),
    ]
