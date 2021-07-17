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
from .forms import FilterFormHelper
from .widgets import PriceRangeWidget, ABVRangeWidget, StarRatingWidget
from django_filters import FilterSet
from django_filters.filters import RangeFilter

class PriceRangeFilter(RangeFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        values = [wine.price for wine in Wine.objects.all()]
        if(min(values) is None):
            min_value = 0.0
        else:
            min_value = min(values)
        if(max(values) is None):
            max_value = 0.0
        else:
            max_value = max(values)
        self.extra['widget'] = PriceRangeWidget(attrs={'data-range_min':min_value,'data-range_max':max_value})

class AbvRangeFilter(RangeFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        values = [wine.abv for wine in Wine.objects.all()]
        if(min(values) is None):
            min_value = 0
        else:
            min_value = min(values)
        if(max(values) is None):
            max_value = 0
        else:
            max_value = max(values)

        self.extra['widget'] = ABVRangeWidget(attrs={'data-range_min':min_value,'data-range_max':max_value})

class StarRatingFilter(RangeFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        values = [wine.rating for wine in Wine.objects.all()]
        if(min(values) is None):
            min_value = 0
        else:
            min_value = min(values)
        if(max(values) is None):
            max_value = 0
        else:
            max_value = max(values)
        self.extra['widget'] = StarRatingWidget(attrs={'data-range_min':min_value,'data-range_max':max_value})

class SliderFilter(FilterSet):
    rating = StarRatingFilter()
    price = PriceRangeFilter()
    abv = AbvRangeFilter()

    class Meta:
        model = Wine
        fields = ['rating', 'price', 'abv']
        form = FilterFormHelper

class WineFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name'
            }
        )
    )

    winery = django_filters.CharFilter(lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Winery'
            }
        )
    )

    vintage = django_filters.ChoiceFilter(choices=Wine.VINTAGE, empty_label="Vintage",
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman; color:#6c757d;',
            }
        )
    )

    bottle = django_filters.ChoiceFilter(choices=Wine.BOTTLE, empty_label="Bottle",
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman; color:#6c757d;',
            }
        )
    )

    closure = django_filters.ChoiceFilter(choices=Wine.CLOSURE, empty_label="Closure",
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman; color:#6c757d;',
            }
        )
    )

    region = django_filters.CharFilter(lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Region'
            }
        )
    )

    type = django_filters.ModelChoiceFilter(queryset=Type.objects.all(), empty_label="Style",
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman; color:#6c757d;',
            }
        )
    )

    country = django_filters.ModelChoiceFilter(queryset=Country.objects.all(), empty_label="Country",
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman; color:#6c757d;',
            }
        )
    )

    grapes = django_filters.ModelMultipleChoiceFilter(queryset=Grapes.objects.all(),
        widget=FilteredSelectMultiple("Grapes", False, attrs={'rows':'10'}))


    bought_from = django_filters.CharFilter(lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Bought from'
            }
        )
    )

    rating = django_filters.NumericRangeFilter(label="Rating range", lookup_expr='range',
        widget=django_filters.widgets.RangeWidget(
            attrs={
                'placeholder': 'Rating starts/ends at'
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

    price = django_filters.NumericRangeFilter(label="Price range", lookup_expr='range',
        widget=django_filters.widgets.RangeWidget(
            attrs={
                'placeholder': 'Price starts/ends at'
            }
        )
    )

    class Meta:
        model = Wine
        fields = ['name', 'winery', 'vintage', 'bottle', 'closure', 'region', 'type', 'country', 'grapes', 'bought_from', 'rating', 'abv', 'price']
        exclude = ['colour', 'aroma', 'taste', 'overall', 'image', 'posted_on', 'drink_by', 'cellar', 'acquired', 'like',]
