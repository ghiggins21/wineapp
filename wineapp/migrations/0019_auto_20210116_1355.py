# Generated by Django 3.0 on 2021-01-16 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wineapp', '0018_auto_20210116_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='drink_by',
            field=models.CharField(blank=True, choices=[('', 'Drink by'), ('Now', 'Now'), ('Sooner', 'Sooner'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031'), ('2032', '2032'), ('2033', '2033'), ('2034', '2034'), ('2035', '2035'), ('2036', '2036'), ('2037', '2037'), ('2038', '2038'), ('2039', '2039'), ('2040', '2040'), ('2041', '2041'), ('2042', '2042'), ('2043', '2043'), ('2044', '2044'), ('2045', '2045'), ('2046', '2046'), ('2047', '2047'), ('2048', '2048'), ('2049', '2049'), ('2050', '2050')], max_length=20, null=True),
        ),
    ]
