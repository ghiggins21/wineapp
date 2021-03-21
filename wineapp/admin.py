from django.contrib import admin

from .models import Wine, Grapes, Country, Type, Notification, Comment, Likes

class WineAdmin(admin.ModelAdmin):

    filter_horizontal = ('grapes',)

admin.site.register(Wine, WineAdmin)
admin.site.register(Grapes)
admin.site.register(Country)
admin.site.register(Type)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(Likes)
