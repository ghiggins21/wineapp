# Generated by Django 3.0 on 2020-09-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wineapp', '0008_auto_20200906_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
