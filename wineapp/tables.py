import django_tables2 as tables
from .models import Wine
from django_tables2.utils import A

class WineTable(tables.Table):
    name = tables.LinkColumn('wine_details', args=[A('pk')])
    class Meta:
        model = Wine
        template_name = "django_tables2/bootstrap4.html"
        fields = ('name', 'winery', 'vintage', 'type', 'country', 'grapes')
        attrs = {"class": "table-striped table-bordered"}
        row_attrs = {

        }
        empty_text = "There are no wines matching the search criteria..."

class CellarWineTable(tables.Table):
    name = tables.LinkColumn('wine_details', args=[A('pk')])
    class Meta:
        model = Wine
        template_name = "django_tables2/bootstrap4.html"
        fields = ('name', 'winery', 'vintage', 'type', 'country', 'grapes', 'cellar')
        attrs = {"class": "table-striped table-bordered"}
        row_attrs = {

        }
        empty_text = "There are no wines matching the search criteria..."
