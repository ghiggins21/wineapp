from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from django import forms
from .models import Wine, Country, Grapes, Type
from django.forms.fields import DateField
from django.conf import settings
import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class WineForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
       super(WineForm, self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.layout = Layout(

           Fieldset(
               'name',
               'winery',
               'vintage',
           ),

           ButtonHolder(
               Submit('submit', 'Submit', css_class='button white')
           )
       )

    def getGrapes(self):
        return grapes

    def getType(self):
        return type


    name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Name",
                    "required": "False"
                }
            )
        )

    winery = forms.CharField(
            required=False,
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Winery"
                }
            )
        )

    vintage = forms.ChoiceField(
            required=False,
            choices=Wine.VINTAGE,
        )

    bottle = forms.ChoiceField(
            required=False,
            choices=Wine.BOTTLE_SIZES
        )

    region = forms.CharField(
            required=False,
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Region"
                }
            )
        )

    type = forms.ModelChoiceField(
            required=False,
            empty_label="Choose style",
            queryset=Type.objects.all()
        )

    country = forms.ModelChoiceField(
            required=False,
            empty_label="Choose country",
            queryset=Country.objects.all()
        )

    grapes = forms.ModelMultipleChoiceField(
            required=False,
            queryset=Grapes.objects.all(),
            widget=FilteredSelectMultiple("Grapes", False, attrs={'rows':'10'})
        )

    cellar = forms.IntegerField(
            required=False,
            label='Cellar',
            widget=forms.NumberInput(
                attrs={
                    'type': 'number',
                    'min': 0,
                    'max': 48,
                    'step': 1,
                    'placeholder': 0
                }
            )
        )

    bought_from = forms.CharField(
            required=False,
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Bought from"
                }
            )
        )
    
    rating = forms.ChoiceField(
            required=False,
            choices=Wine.RATING,
            widget=forms.RadioSelect()
            )
        

    abv = forms.DecimalField(
            required=False,
            label='ABV',
            widget=forms.TextInput(
                attrs={
                    'type': 'number',
                    'min': 5.0,
                    'max': 24.0,
                    'step': 0.5,
                    'placeholder': 5.0
                }
            )
        )

    price = forms.FloatField(
            required=False,
            label='Price (£)',
            widget=forms.NumberInput(
                attrs={
                    'type': 'number',
                    'min': 5.00,
                    'max': 1000.00,
                    'step': 0.05,
                    'placeholder': 5.00
                }
            )
        )

    colour = forms.CharField(
            required=False,
            widget=forms.Textarea(
                attrs={
                    "placeholder": "Colour",
                    "rows": 2,
                    "cols": 1
                    }
                )
            )

    aroma = forms.CharField(
            required=False,
            widget=forms.Textarea(
                attrs={
                    "placeholder": "Add aroma",
                    "rows": 2,
                    "cols": 15
                    }
                )
            )

    taste = forms.CharField(
            required=False,
            widget=forms.Textarea(
                attrs={
                    "placeholder": "Taste",
                    "rows": 3,
                    "cols": 10
                    }
                )
            )
    overall = forms.CharField(
            required=False,
            widget=forms.Textarea(
                attrs={
                    "placeholder": "Overall",
                    "rows": 3,
                    "cols": 1
                    }
                )
            )

    acquired = forms.DateField(
            required=False,
            input_formats=settings.DATE_INPUT_FORMATS,
            widget=forms.DateInput(
                attrs={
                    "type": "date"
                }
            )
        )

    drink_by = forms.IntegerField(
            required=False,
            widget=forms.Select(
                choices=Wine.DRINK_BY,
                attrs={
                    "placeholder": "Drink by"
                }
            )
        )

    image = forms.ImageField(
            required=False
    )

    class Meta:
        model = Wine
        fields = [
            'name',
            'winery',
            'vintage',
            'bottle',
            'region',
            'type',
            'country',
            'grapes',
            'cellar',
            'bought_from',
            'rating',
            'abv',
            'price',
            'colour',
            'aroma',
            'taste',
            'overall',
            'acquired',
            'drink_by',
            'image'
        ]

        fieldsets = (
            ("Review", {
                'fields': ('colour', 'aroma', 'taste', 'overall'),
            }),
        )

    class Media:
        css = {'all': ('/static/admin/css/widgets.css',),}
        #js = ('/admin/jsi18n',)
