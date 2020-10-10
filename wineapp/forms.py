from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms
from .models import Wine, Country, Grapes, Type
from django.conf import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

class WineForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
       super(WineForm, self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.form_show_labels = False

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
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman',
            }
        )
    )

    bottle = forms.ChoiceField(
        required=False,
        choices=Wine.BOTTLE_SIZES,
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman',
            }
        )
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
        queryset=Type.objects.all(),
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman',
            }
        )
    )

    country = forms.ModelChoiceField(
        required=False,
        empty_label="Choose country",
        queryset=Country.objects.all(),
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman',
            }
        )
    )

    grapes = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Grapes.objects.all(),
        widget=FilteredSelectMultiple("Grapes", False)
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
                'placeholder': 'Cellar'
            }
        )
    )

    bought_from = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Bought from",
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
                'placeholder': 'ABV'
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
                'placeholder': 'Price'
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
                "placeholder": "Aroma",
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

        )
    )

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "placeholder": "Add image",
                'style': 'font-family: Times New Roman',
            }
        )
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

    #class Media:
        #css = {'all': ('/static/admin/css/widgets.css',),}
        #js = ('/admin/jsi18n',)
