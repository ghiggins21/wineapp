# Generated by Django 3.0 on 2021-05-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wineapp', '0008_auto_20210528_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
