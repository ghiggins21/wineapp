# Generated by Django 3.0 on 2021-07-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wineapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='closure',
            field=models.CharField(choices=[('', 'Closure'), ('None', 'None'), ('Agglomerate cork', 'Agglomerate cork'), ('Colmate cork', 'Colmate cork'), ('Diam cork 2', 'Diam cork 2'), ('Diam cork 3', 'Diam cork 3'), ('Diam cork 5', 'Diam cork 5'), ('Diam cork 10', 'Diam cork 10'), ('Synthetic cork', 'Synthetic cork'), ('Natural cork', 'Natural cork'), ('Champagne/Sparkling wine cork', 'Champagne/Sparkling wine cork'), ('Crown cap', 'Crown cap'), ('Glass stopper', 'Glass stopper'), ('Helix', 'Helix'), ('Stopper cork', 'Stopper cork'), ('Screwcap', 'Screwcap'), ('Twin top', 'Twin top'), ('Vinoseal/Vinolok', 'Vinoseal/Vinolok'), ('Zork', 'Zork')], default='', max_length=35),
        ),
    ]
