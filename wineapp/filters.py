from django.contrib.admin.widgets import FilteredSelectMultiple
import django_filters
from django import forms
from django.forms import ModelForm
from .forms import WineForm
from .models import Wine, Grapes, Type, Country
from django.conf import settings
from django.forms.fields import DateField
import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class WineFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')
    winery = django_filters.CharFilter(lookup_expr='icontains')
    vintage = django_filters.ChoiceFilter(choices=Wine.VINTAGE, empty_label="Choose vintage")
    country = django_filters.ModelChoiceFilter(queryset=Country.objects.all(), empty_label="Choose country")
    region = django_filters.CharFilter(lookup_expr='icontains')
    rating = django_filters.ChoiceFilter(choices=Wine.RATING, empty_label="Choose rating")
    rating_gt = django_filters.NumberFilter(field_name='rating_gt', lookup_expr='gt')
    rating_lt = django_filters.NumberFilter(field_name='rating_lt', lookup_expr='lt')
    price = django_filters.NumericRangeFilter(label="Price range", lookup_expr='range')
    bought_from = django_filters.CharFilter(lookup_expr='icontains')
    abv = django_filters.NumericRangeFilter(label="ABV Range", lookup_expr='range')
    grapes = django_filters.ModelMultipleChoiceFilter(queryset=Grapes.objects.all(),
        widget=FilteredSelectMultiple("Grapes", False, attrs={'rows':'10'}))
    type = django_filters.ModelChoiceFilter(queryset=Type.objects.all(), empty_label="Choose style")
    bottle = django_filters.ChoiceFilter(choices=Wine.BOTTLE_SIZES, empty_label="Choose botte size")

    class Meta:
        model = Wine
        fields = ['name', 'winery', 'vintage', 'country', 'region', 'rating', 'price', 'bought_from', 'abv', 'grapes', 'type', 'bottle']
        exclude = ['colour', 'aroma', 'taste', 'overall', 'image', 'posted_on', 'drink_by', 'cellar', 'acquired']
