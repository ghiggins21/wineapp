from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import WineForm
from .filters import WineFilter
from .models import Wine
from .tables import WineTable
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django_tables2 import SingleTableView
from django_tables2.config import RequestConfig
from django.db.models import Q,Count
from django.contrib import messages
import datetime
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string

def home(request, *args, **kwargs):
    type = Wine.objects.values('type__name').exclude(type=None).annotate(total=Count('type__name')).order_by('type__name') or 0
    country = Wine.objects.values('country__name').exclude(country=None).annotate(total=Count('country__name')).order_by('country__name') or 0
    ratings = Wine.objects.values('rating').annotate(total=Count('rating')).order_by('rating') or 0
    g = Wine.objects.values('grapes__name').annotate(total=Count('grapes')).order_by('grapes') or 0

    wine_count = Wine.objects.all().count()
    wine_ratings = Wine.objects.filter(rating__gt=0).count()
    in_cellar = Wine.objects.filter(cellar__gt=0).count()
    if(wine_count > 0):
        last_review = Wine.objects.latest('posted_on')
        grapes = last_review.grapes.all()
        type_name = last_review.type
        stars = last_review.rating
        country_name = last_review.country

        context = {
            'type': type,
            'ratings': ratings,
            'g': g,
            'grapes': grapes,
            'wine_ratings': wine_ratings,
            'wine_count': wine_count,
            'in_cellar': in_cellar,
            'country': country,
            'range': range(10),
            'last_review': last_review,
            'type_name': str(type_name),
            'country_name': str(country_name)
        }
        return render(request, "wineapp/home.html", context)
    else:
        return render(request, "wineapp/home.html")

def wine_list(request):
    table = WineTable(Wine.objects.all())
    RequestConfig(request, paginate={"per_page": 10 }).configure(table)

    context = {
        'table': table
    }

    return render(request, "wineapp/wine_list.html", context)

def add_wine(request, *args, **kwargs):
    if request.method == 'POST':

        form = WineForm(request.POST, request.FILES)

        if form.is_valid():
            data = request.POST.copy()
            form.save()
            messages.success(request, data.get('name') + " has been saved successfully.")
            return redirect('show_messages')
        else:
            form = WineForm()
            messages.error(request, 'Wine was not saved')
            return redirect(request, "wineapp/add_wine.html")
    else:
        form = WineForm()

    context = {
        'form': form,
    }
    return render(request, "wineapp/add_wine.html", context)

def edit_wine(request, id):
    wine = get_object_or_404(Wine, id=id)
    wine_overall = wine.overall
    if request.method == "POST":
        form = WineForm(request.POST, request.FILES, instance=wine)
        if form.is_valid():
            data = request.POST.copy()
            wine = form.save(commit=False)
            if wine_overall != data.get('overall'):
                wine.posted_on = datetime.datetime.now()
            wine.save()
            form.save_m2m()
            messages.success(request, data.get('name') + " has been edited successfully.")
            return redirect('show_messages')
        else:
            form = WineForm(instance=wine)
            messages.error(request, 'Wine was not saved')
            return redirect(request, "wineapp/add_wine.html")

        #return redirect('wine_details', id=wine.id)
    else:
        form = WineForm(instance=wine)
    return render(request, 'wineapp/add_wine.html', {'form': form})

def wine_details(request, id):
    rating_string = {
      1 : "Expired",
      2 : "Awful",
      3 : "Poor",
      4 : "So-so",
      5 : "Fair",
      6 : "Good",
      7 : "Very good",
      8 : "Excellent",
      9 : "Fantastic",
      10 : "Blockbuster",
    }

    wine = get_object_or_404(Wine, id=id)
    wine = Wine.objects.get(pk=id)
    grapes = wine.grapes.all()
    style = str(wine.type)
    country = str(wine.country)

    context = {
        'range': range(10),
        'wine': wine,
        'style': style,
        'country': country,
        'grapes': grapes,
        'rating_string': rating_string
    }
    return render(request, "wineapp/wine_details.html", context)

def about(request, *args, **kwargs):
    about_wineapp = {
        "name": "Wine or Whine",
        "author": "Author: Gabriel aka Vinus de Wino",
        "email": "Email: gabehiggins21@gmail.com",
        "phone": "Phone: +44(0)7765183528",
        "disclaimer": "Disclaimer: This is just my opinion on the wines I have tried. Like all wine reviews they are subjective and my reviews should not influence your wine buying options.",
    }
    return render(request, "wineapp/about.html", about_wineapp)

def delete_wine(request, id):
    if 'Cancel' in request.POST:
        return HttpResponseRedirect('wine_details', id=wine.id)
    wine = get_object_or_404(Wine, id=id)
    if request.method == "POST":
        messages.info(request, wine.name + " has been deleted successfully.")
        # confirming delete
        wine.delete()

        return redirect('show_messages')
    context = {
        "wine": wine
    }
    return render(request, "wineapp/delete_wine.html", context)

def cellar(request):
    table = WineTable(Wine.objects.filter(cellar__gt=0))
    RequestConfig(request, paginate={"per_page": 10}).configure(table)

    context = {
        'table': table
    }
    return render(request, "wineapp/cellar.html", context)

def rating(request):
    table = WineTable(Wine.objects.filter(rating__gt=0))
    RequestConfig(request, paginate={"per_page": 10}).configure(table)

    context = {
        'table': table
    }
    return render(request, "wineapp/rating.html", context)

def wine_filter(request):
    wines= Wine.objects.all()
    filter = WineFilter(request.GET, queryset = wines)
    has_filter = any(field in request.GET for field in set(filter.get_fields()))
    table = WineTable(filter.qs)

    RequestConfig(request, paginate={"per_page": 10}).configure(table)

    context = {
        'table': table,
        'filter': filter,
        'has_filter': has_filter
    }
    return render(request, 'wineapp/wine_filter.html', context)


def search_wines(request):

    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(name__icontains=query) | Q(vintage__icontains=query)

            results= Wine.objects.filter(lookups).distinct()
            table = WineTable(results)
            table.paginate(page=request.GET.get('page', 1), per_page=10)
            RequestConfig(request).configure(table)
            context = {
                'table': table,
                'submitbutton': submitbutton
            }
            return render(request, "wineapp/search.html", context)


            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'wineapp/search.html', context)


        else:
            return render(request, 'wineapp/search.html')

    else:
        return render(request, 'wineapp/search.html')

def show_messages(request):
    return render(request, "wineapp/show_messages.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "registration/login.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))
        else:
             return render(request, "registration/login.html")
'''

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "registration/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}

                    #During production, the domain, site name, protocol, and from email address will need to be changed.
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="registration/password_reset.html", context={"password_reset_form":password_reset_form})
'''
