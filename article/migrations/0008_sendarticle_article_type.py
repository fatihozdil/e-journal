# Generated by Django 2.1.5 on 2021-05-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_sendarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendarticle',
            name='article_type',
            field=models.TextField(choices=[('articleType1', 'Röportaj'), ('articleType2', 'Haber'), ('articleType3', 'Makale'), ('articleType4', 'Diğer')], default='articleType1', max_length=10),
        ),
    ]
