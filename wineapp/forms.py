from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms
from .models import Wine, Country, Grapes, Type, Comment
from django.conf import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth.forms import UserCreationForm
from django_filters.fields import RangeField
from crispy_forms.bootstrap import StrictButton

class FilterFormHelper(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'get'
        self.fields['abv'].label = "ABV"
        layout_fields = []
        for field_name, field in self.fields.items():
            if isinstance(field, RangeField):
                layout_field = Field(field_name, template="wineapp/crispy-range-slider.html")
            else:
                layout_field = Field(field_name)
            layout_fields.append(layout_field)
        #layout_fields.append(StrictButton("Submit", name='submit', type='submit', css_class='btn btn-fill-out btn-block mt-1'))
        self.helper.layout = Layout(*layout_fields)


class WineForm(forms.ModelForm):

    class Meta:
        model = Wine
        fields = [
            'name',
            'winery',
            'vintage',
            'bottle',
            'closure',
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
            'image',
        ]


    def __init__(self, *args, **kwargs):

       helper = self.helper = FormHelper()
       self.helper.form_method = 'post'
       layout = helper.layout = Layout()
       self.helper.form_show_labels = False
       super(WineForm, self).__init__(*args, **kwargs)

    def getGrapes(self):
        return grapes

    def getType(self):
        return type


    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
            }
        )
    )

    winery = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Winery"
            }
        )
    )

    vintage = forms.ChoiceField(
        required=True,
        choices=Wine.VINTAGE,
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman;',
                "placeholder": "ZZZZZZ",
            }
        )
    )

    bottle = forms.ChoiceField(
        required=True,
        choices=Wine.BOTTLE,
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman;',
            }
        )
    )

    closure = forms.ChoiceField(
        required=False,
        choices=Wine.CLOSURE,
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman;',
            }
        )
    )

    region = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Region"
            }
        )
    )

    type = forms.ModelChoiceField(
        required=True,
        empty_label="Style",
        queryset=Type.objects.all(),
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman;',
            }
        )
    )

    country = forms.ModelChoiceField(
        required=True,
        empty_label="Country",
        queryset=Country.objects.all(),
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman;',
            }
        )
    )

    grapes = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Grapes.objects.all(),
        widget=FilteredSelectMultiple("Grapes", False,
            attrs={
                'style': 'font-family: Times New Roman;',
            }
        )
    )

    cellar = forms.IntegerField(
        required=True,
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
        required=True,
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

    abv = forms.FloatField(
        required=True,
        label='ABV',
        widget=forms.NumberInput(
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
        required=True,
        label='Price (£)',
        widget=forms.NumberInput(
            attrs={
                'type': 'number',
                'min': 1.00,
                'max': 1000.00,
                'step': 0.05,
                'placeholder': 'Price £',
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
        required=True,
        input_formats=settings.DATE_INPUT_FORMATS,
        widget=forms.DateInput(
            attrs={
                "type": "date"
            }
        )
    )

    drink_by = forms.ChoiceField(
        required=True,
        choices=Wine.DRINK_BY,
        widget=forms.Select(
            attrs={
                'style': 'font-family: Times New Roman;',
                }
        )
    )

    image = forms.ImageField(
        required=False,
    )

    class Media:
        css = {'all': ('/static/admin/css/widgets.css',),}
        js = ('/admin/jsi18n',)

class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('pretty.css',)
        }
        js = ('animations.js', 'actions.js')

class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', "required": "True"}), max_length=64, help_text='Enter a valid email address')

    class Meta(UserCreationForm.Meta):
        email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email*", "required": "True"}), max_length=64, help_text='Enter a valid email address')
        fields = UserCreationForm.Meta.fields + ("email",)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):

        helper = self.helper = FormHelper()
        self.helper.form_method = 'post'
        layout = helper.layout = Layout()

        self.helper.form_show_labels = False
        super(CommentForm, self).__init__(*args, **kwargs)

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                "placeholder": "Comment",
                "rows": 3,
                "cols": 1,
            }
        )
    )
