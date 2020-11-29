from django.db import models
import datetime
from django.urls import reverse

class Wine(models.Model):

    VINTAGE = []
    VINTAGE.append(("Unknown", "Unknown"))
    VINTAGE.append(("NV", "NV"))
    VINTAGE.append(("Solera System", "Solera System"))
    for y in reversed(range(1875, (datetime.datetime.now().year + 1))):
        VINTAGE.append((str(y), str(y)))
    VINTAGE = [('','Vintage')] + VINTAGE

    DRINK_BY = []
    for y in range(datetime.datetime.now().year, (datetime.datetime.now().year + 30)):
        DRINK_BY.append((str(y), str(y)))
    DRINK_BY = [('','Drink by')] + DRINK_BY

    BOTTLE_SIZES = [
        ('Split (187ml)', 'Split (187ml)'),
        ('Quarter (200ml)', 'Quarter (200ml)'),
        ('Half (375ml)', 'Half (375ml)'),
        ('Jennie (500ml)', 'Jennie (500ml)'),
        ('Clavelin (620ml)', 'Clavelin (620ml)'),
        ('Standard (750ml)', 'Standard (750ml)'),
        ('Litre (1L)', 'Litre (1L)'),
        ('Magnum (1.5L)', 'Magnum (1.5L)'),
        ('Jeroboam (3L)', 'Jeroboam (3L)'),
        ('Rehoboam (4.5L)', 'Rehoboam (4.5L)'),
        ('Methuselah (6L)', 'Methuselah (6L)'),
        ('Imperial (6L)', 'Imperial (6L)'),
        ('Salmanazar (9L)', 'Salmanazar (9L)'),
        ('Balthazar (12L)', 'Balthazar (12L)'),
        ('Nebuchadnezzar (15L)', 'Nebuchadnezzar (15L)'),
        ('Melchior (18L)', 'Melchior (18L)'),
        ('Solomon (20L)', 'Solomon (20L)'),
        ('Sovereign (26L)', 'Sovereign (26L)'),
        ('Goliath (27L)', 'Goliath (27L)'),
        ('Melchizedek (30L)', 'Melchizedek (30L)'),
    ]
    BOTTLE_SIZES = [('','Choose bottle size')] + BOTTLE_SIZES

    RATING =[
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    ]


    def __str__ (self):
        return self.name

    name = models.CharField(max_length=255, blank=False, unique=False)
    winery = models.CharField(max_length=100, blank=True, null=True)
    vintage = models.CharField(choices=VINTAGE, max_length=20, blank=True, null=True)
    bottle = models.CharField(choices=BOTTLE_SIZES, max_length=100, blank=True, null=True, default=None)
    region = models.CharField(max_length=100, blank=True, null=True)
    type = models.ForeignKey('type', max_length=50, blank=True, null=True, default="", on_delete=models.CASCADE)
    country = models.ForeignKey('country', blank=True, null=True, default="", on_delete=models.CASCADE)
    grapes = models.ManyToManyField('grapes', blank=True, related_name='grape_set')
    cellar = models.IntegerField(blank=True, null=True, default=0)
    bought_from = models.CharField(max_length=100, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(choices=RATING, null=True, default=0)
    abv = models.FloatField(default=0.0, blank=True, null=True)
    price = models.FloatField(null=True, blank=True, default=0.0)
    colour = models.TextField(blank=True, null=True)
    aroma = models.TextField(blank=True, null=True)
    taste = models.TextField(blank=True, null=True)
    overall = models.TextField(blank=True, null=True)
    acquired = models.DateField(blank=True, null=True)
    drink_by = models.CharField(choices=DRINK_BY, max_length=20, blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    image = models.ImageField(max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("wine_details", kwargs={"id": self.id})

    success_message = "%(name)s was created successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )

    class Meta:
        get_latest_by = 'posted_on'


class Grapes(models.Model):
    class Meta:
        verbose_name_plural = "Grapes"
        ordering = ['name']

    def __str__ (self):
        return self.name

    name = models.CharField(max_length=200)

class Country(models.Model):

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name']

    def __str__ (self):
        return self.name

    name = models.CharField(max_length=30)

class Type(models.Model):

    class Meta:
        verbose_name_plural = "Type"

    def __str__ (self):
        return self.name

    name = models.CharField(max_length=30)
