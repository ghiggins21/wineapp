# Generated by Django 3.0 on 2021-01-16 13:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wineapp', '0017_wine_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='likes',
            field=models.ManyToManyField(related_name='wine_review', to=settings.AUTH_USER_MODEL),
        ),
    ]
