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
from django import forms


class WineFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name contains'
            }
        )
    )

    winery = django_filters.CharFilter(lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Winery contains'
            }
        )
    )
    vintage = django_filters.ChoiceFilter(choices=Wine.VINTAGE, empty_label="Choose vintage",
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman',
            }
        )
    )
    country = django_filters.ModelChoiceFilter(queryset=Country.objects.all(), empty_label="Choose country",
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman',
            }
        )
    )
    region = django_filters.CharFilter(lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Region contains'
            }
        )
    )
    rating = django_filters.ChoiceFilter(choices=Wine.RATING, empty_label="Choose rating",
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman',
            }
        )
    )
    rating_gt = django_filters.NumberFilter(field_name='rating_gt', lookup_expr='gt')
    rating_lt = django_filters.NumberFilter(field_name='rating_lt', lookup_expr='lt')
    price = django_filters.NumericRangeFilter(label="Price range", lookup_expr='range',
        widget=django_filters.widgets.RangeWidget(
            attrs={
                'placeholder': 'Price starts/ends at'
            }
        )
    )
    bought_from = django_filters.CharFilter(lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Bought from contains'
            }
        )
    )
    abv = django_filters.NumericRangeFilter(label="ABV Range", lookup_expr='range',
        widget=django_filters.widgets.RangeWidget(
            attrs={
                'placeholder': 'ABV starts/ends at'
            }
        )
    )
    grapes = django_filters.ModelMultipleChoiceFilter(queryset=Grapes.objects.all(),
        widget=FilteredSelectMultiple("Grapes", False, attrs={'rows':'10'}))
    type = django_filters.ModelChoiceFilter(queryset=Type.objects.all(), empty_label="Choose style",
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman',
            }
        )
    )
    bottle = django_filters.ChoiceFilter(choices=Wine.BOTTLE_SIZES, empty_label="Choose botte size",
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman',
            }
        )
    )

    class Meta:
        model = Wine
        fields = ['name', 'winery', 'vintage', 'country', 'region', 'rating', 'price', 'bought_from', 'abv', 'grapes', 'type', 'bottle']
        exclude = ['colour', 'aroma', 'taste', 'overall', 'image', 'posted_on', 'drink_by', 'cellar', 'acquired']
