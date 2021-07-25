# Generated by Django 2.2.20 on 2021-07-23 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wineapp', '0014_auto_20210723_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='closure',
            field=models.CharField(choices=[('', 'Closure'), ('None', 'None'), ('Unknown', 'Unknown'), ('Agglomerate cork', 'Agglomerate cork'), ('Colmate cork', 'Colmate cork'), ('Diam 2 cork', 'Diam 2 cork'), ('Diam 3 cork', 'Diam 3 cork'), ('Diam 5 cork', 'Diam 5 cork'), ('Diam 10 cork', 'Diam 10 cork'), ('Synthetic cork', 'Synthetic cork'), ('Natural cork', 'Natural cork'), ('Champagne/Sparkling wine cork', 'Champagne/Sparkling wine cork'), ('Crown cap', 'Crown cap'), ('Glass stopper', 'Glass stopper'), ('Helix', 'Helix'), ('Stopper cork', 'Stopper cork'), ('Screwcap', 'Screwcap'), ('Twin top', 'Twin top'), ('Vinoseal/Vinolok', 'Vinoseal/Vinolok'), ('Zork', 'Zork')], max_length=100, null=True),
        ),
    ]
