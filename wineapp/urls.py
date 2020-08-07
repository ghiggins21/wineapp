"""wineapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.i18n import JavaScriptCatalog
from django.conf.urls import include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
#from wineapp.views import WineChartView #WineListView

from wineapp.views import (
    home,
    add_wine,
    wine_list,
    wine_details,
    about,
    delete_wine,
    edit_wine,
    cellar,
    rating,
    wine_filter,
    search_wines,
    show_messages,
    )

app_name = 'wineapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    #path('wineapp/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', home, name='home'),
    path('wine_list/', wine_list, name='wine_list'),
    path('add_wine/', add_wine, name='add_wine'),
    path('wine_filter/', wine_filter, name='wine_filter'),
    path('<int:id>/edit_wine/', edit_wine, name='edit_wine'),
    path('<int:id>/wine_details/', wine_details, name='wine_details'),
    path('about/', about, name='about'),
    path('<int:id>/delete_wine/', delete_wine, name='delete_wine'),
    path('admin/jsi18n/', JavaScriptCatalog.as_view(), name='java-script-catalog'),
    path('search/', search_wines, name='search'),
    path('cellar/', cellar, name='cellar'),
    path('rating/', rating, name='rating'),
    path('show_messages/', show_messages, name='show_messages'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
