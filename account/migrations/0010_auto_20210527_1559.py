# Generated by Django 2.1.5 on 2021-05-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20210527_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_avatar',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Fotoğraf ekle'),
        ),
    ]
