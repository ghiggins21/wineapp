# Generated by Django 3.0 on 2021-07-11 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wineapp', '0006_auto_20210710_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='closure',
        ),
    ]
