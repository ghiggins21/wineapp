import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.urls import reverse
from django.db.models.signals import post_save, post_delete

class Wine(models.Model):

    VINTAGE = []
    VINTAGE.append(('','Vintage'))
    VINTAGE.append(("Unknown", "Unknown"))
    VINTAGE.append(("NV", "NV"))
    VINTAGE.append(("MV", "MV"))
    VINTAGE.append(("Solera System", "Solera System"))
    for y in reversed(range(1875, (datetime.datetime.now().year + 1))):
        VINTAGE.append((str(y), str(y)))

    DRINK_BY = []
    DRINK_BY.append(('','Drink by'))
    DRINK_BY.append(("Now", "Now"))
    DRINK_BY.append(("Sooner", "Sooner"))
    for y in range(datetime.datetime.now().year, (datetime.datetime.now().year + 30)):
        DRINK_BY.append((str(y), str(y)))

    BOTTLE = [
        ('','Bottle'),
        ('Can', 'Can'),
        ('Box', 'Box'),
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

    RATING =[
        (0, 0),
        (.5, .5),
        (1, 1),
        (1.5, 1.5),
        (2, 2),
        (2.5, 2.5),
        (3, 3),
        (3.5, 3.5),
        (4, 4),
        (4.5, 4.5),
        (5, 5),
        (5.5, 5.5),
        (6, 6),
        (6.5, 6.5),
        (7, 7),
        (7.5, 7.5),
        (8, 8),
        (8.5, 8.5),
        (9, 9),
        (9.5, 9.5),
        (10, 10),
    ]

    CLOSURE =[
        ('', 'Closure'),
        ('None', 'None'),
        ('Agglomerate cork', 'Agglomerate cork'),
        ('Colmate cork', 'Colmate cork'),
        ('Diam cork 2', 'Diam cork 2'),
        ('Diam cork 3', 'Diam cork 3'),
        ('Diam cork 5', 'Diam cork 5'),
        ('Diam cork 10', 'Diam cork 10'),
        ('Synthetic cork', 'Synthetic cork'),
        ('Natural cork', 'Natural cork'),
        ('Champagne/Sparkling wine cork', 'Champagne/Sparkling wine cork'),
        ('Crown cap', 'Crown cap'),
        ('Glass stopper', 'Glass stopper'),
        ('Helix', 'Helix'),
        ('Stopper cork', 'Stopper cork'),
        ('Screwcap', 'Screwcap'),
        ('Twin top', 'Twin top'),
        ('Vinoseal/Vinolok','Vinoseal/Vinolok'),
        ('Zork', 'Zork'),
    ]

    def __str__ (self):
        return self.name

    name = models.CharField(max_length=255, blank=False, unique=False)
    winery = models.CharField(max_length=100, blank=False)
    vintage = models.CharField(choices=VINTAGE, max_length=20, null=False, blank=False)
    bottle = models.CharField(choices=BOTTLE, max_length=75, null=True, blank=False)
    region = models.CharField(max_length=100, blank=False)
    type = models.ForeignKey('type', max_length=25, blank=True, null=True, on_delete=models.CASCADE)
    country = models.ForeignKey('country', blank=True, default="", null=True, on_delete=models.CASCADE)
    closure = models.CharField(choices=CLOSURE, max_length=100, null=True, blank=False)
    grapes = models.ManyToManyField('grapes', blank=False, related_name='grape_set')
    cellar = models.IntegerField(blank=True, null=True, default=0)
    bought_from = models.CharField(max_length=100, blank=False, default='')
    rating = models.FloatField(choices=RATING, null=True, blank=True, default=0.0)
    abv = models.FloatField(null=False, blank=False, default=0.0)
    price = models.FloatField(null=False, blank=False, default=0.0)
    colour = models.TextField(blank=True, default='')
    aroma = models.TextField(blank=True, default='')
    taste = models.TextField(blank=True, default='')
    overall = models.TextField(blank=True, default='')
    acquired = models.DateField(blank=False, null=True)
    drink_by = models.CharField(choices=DRINK_BY, max_length=20, blank=False, default='')
    posted_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    image = models.ImageField(max_length=255, blank=True, null=True)
    like = models.IntegerField(default=0)

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
        ordering = ['-id']

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

class Notification(models.Model):
    NOTIFICATION_TYPES = ((1,'Like'),(2,'Comment'),(3,'Follow'))
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name="noti_wine", blank=True, null=True)
    sender = models.ForeignKey(User, blank=True, null=True, default="", on_delete=models.CASCADE, related_name="noti_from_user")
    user = models.ForeignKey(User, blank=True, null=True, default="", on_delete=models.CASCADE, related_name="noti_to_user")
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    text_preview = models.CharField(max_length=90, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

class Likes(models.Model):

    class Meta:
        verbose_name_plural = "Likes"

    wine = models.ForeignKey(Wine, blank=True, null=True, default="", on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='like_from_user')

    def user_liked_review(sender, instance, *args, **kwargs):
        like = instance
        wine = like.wine
        sender = like.user
        notify = Notification(wine=wine, sender=sender, user=wine.user, notification_type=1)
        notify.save()

    def user_unlike_review(sender, instance, *args, **kwargs):
        like = instance
        wine = like.wine
        sender = like.user

        notify = Notification.objects.filter(wine=wine, sender=sender, notification_type=1)
        notify.delete()

#Likes
post_save.connect(Likes.user_liked_review, sender=Likes)
post_delete.connect(Likes.user_unlike_review, sender=Likes)

class Comment(models.Model):

    class Meta:
        verbose_name_plural = "Comment"

    wine = models.ForeignKey(Wine, blank=True, null=True, default="", on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='comment_from_user')
    name = models.CharField(max_length=255)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.name)

    def user_comment_review(sender, instance, *args, **kwargs):
        comment = instance
        wine = comment.wine
        text_preview = comment.text[:90]
        sender = comment.user
        notify = Notification(wine=wine, sender=sender, user=wine.user, text_preview=text_preview , notification_type=2)
        notify.save()

    def user_del_comment_review(sender, instance, *args, **kwargs):
        comment = instance
        wine = comment.wine
        sender = comment.user

        notify = Notification.objects.filter(wine=wine, sender=sender, notification_type=2)
        notify.delete()

#Comment
post_save.connect(Comment.user_comment_review, sender=Comment)
post_delete.connect(Comment.user_del_comment_review, sender=Comment)
