from django.contrib import admin

from .models import Wine, Grapes, Country, Type, Comment

class WineAdmin(admin.ModelAdmin):
    '''
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Winery', {'fields': ['winery'], 'classes': ['collapse']}),
        ('Vintage', {'fields': ['vintage'], 'classes': ['collapse']}),
        ('Region', {'fields': ['region'], 'classes': ['collapse']}),
        ('Type', {'fields': ['type'], 'classes': ['collapse']}),
        ('Bottle', {'fields': ['bottle'], 'classes': ['collapse']}),
        ('Country', {'fields': ['country'], 'classes': ['collapse']}),
        ('Grapes', {'fields': ['grapes'], 'classes': ['collapse']}),
        ('Cellar', {'fields': ['cellar'], 'classes': ['collapse']}),
        ('Bought_from', {'fields': ['bought_from'], 'classes': ['collapse']}),
        ('Rating', {'fields': ['rating'], 'classes': ['collapse']}),
        ('ABV', {'fields': ['abv'], 'classes': ['collapse']}),
        ('Price', {'fields': ['price'], 'classes': ['collapse']}),
        ('Colour', {'fields': ['colour'], 'classes': ['collapse']}),
        ('Aroma', {'fields': ['aroma'], 'classes': ['collapse']}),
        ('Taste', {'fields': ['taste'], 'classes': ['collapse']}),
        ('Overall', {'fields': ['overall'], 'classes': ['collapse']}),
        ('Acquired', {'fields': ['acquired'], 'classes': ['collapse']}),
        ('Drink by', {'fields': ['drink_by'], 'classes': ['collapse']}),
        #('Posted on', {'fields': ['posted_on'], 'classes': ['collapse']}),
        ('Image', {'fields': ['image']}),

    ]
    '''
    filter_horizontal = ('grapes',)

admin.site.register(Wine, WineAdmin)
admin.site.register(Grapes)
admin.site.register(Country)
admin.site.register(Type)
admin.site.register(Comment)
