# Generated by Django 3.0 on 2021-07-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wineapp', '0012_auto_20210716_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='bottle',
            field=models.CharField(choices=[('', 'Bottle Size'), ('Can', 'Can'), ('Box', 'Box'), ('Split (187ml)', 'Split (187ml)'), ('Quarter (200ml)', 'Quarter (200ml)'), ('Half (375ml)', 'Half (375ml)'), ('Jennie (500ml)', 'Jennie (500ml)'), ('Clavelin (620ml)', 'Clavelin (620ml)'), ('Standard (750ml)', 'Standard (750ml)'), ('Litre (1L)', 'Litre (1L)'), ('Magnum (1.5L)', 'Magnum (1.5L)'), ('Jeroboam (3L)', 'Jeroboam (3L)'), ('Rehoboam (4.5L)', 'Rehoboam (4.5L)'), ('Methuselah (6L)', 'Methuselah (6L)'), ('Imperial (6L)', 'Imperial (6L)'), ('Salmanazar (9L)', 'Salmanazar (9L)'), ('Balthazar (12L)', 'Balthazar (12L)'), ('Nebuchadnezzar (15L)', 'Nebuchadnezzar (15L)'), ('Melchior (18L)', 'Melchior (18L)'), ('Solomon (20L)', 'Solomon (20L)'), ('Sovereign (26L)', 'Sovereign (26L)'), ('Goliath (27L)', 'Goliath (27L)'), ('Melchizedek (30L)', 'Melchizedek (30L)')], max_length=75, null=True),
        ),
    ]
