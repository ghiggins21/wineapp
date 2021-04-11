from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import WineForm, CommentForm
from .filters import WineFilter
from .models import Wine, Notification, Comment, Likes
from .tables import WineTable
from django.http import HttpResponseRedirect, JsonResponse
from django_tables2 import SingleTableView
from django_tables2.config import RequestConfig
from django.db.models import Q,Count
from django.contrib import messages
import pytz
from django.utils import timezone
from datetime import datetime
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.core.paginator import Paginator

def home(request, *args, **kwargs):
    type = Wine.objects.values('type__name').exclude(type=None).annotate(total=Count('type__name')).order_by('type__name') or 0
    country = Wine.objects.values('country__name').exclude(country=None).annotate(total=Count('country__name')).order_by('country__name') or 0
    ratings = Wine.objects.values('rating').annotate(total=Count('rating')).order_by('rating') or 0
    vintage = Wine.objects.values('vintage').annotate(total=Count('vintage')).order_by('vintage') or 0
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
            'vintage': vintage,
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

    wine_list = Wine.objects.all()
    paginator = Paginator(wine_list, 10)
    page_number = request.GET.get('page')
    wines = paginator.get_page(page_number)

    context = {
        'table': table,
        'wines': wines,
    }

    return render(request, "wineapp/wine_list.html", context)

def add_wine(request, *args, **kwargs):
    if 'Cancel' in request.POST:
        return HttpResponseRedirect('wine_details', id=wine.id)
    if request.method == 'POST':

        form = WineForm(request.POST, request.FILES)

        if form.is_valid():
            wine = form.save(commit=False)
            wine.user = request.user
            data = request.POST.copy()

            wine.save()
            form.save_m2m()

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
    if 'Cancel' in request.POST:
        return HttpResponseRedirect('wine_details', id=wine.id)
    wine = get_object_or_404(Wine, id=id)
    wine_overall = wine.overall
    if request.method == "POST":
        form = WineForm(request.POST, request.FILES, instance=wine)
        if form.is_valid():
            data = request.POST.copy()
            wine = form.save(commit=False)
            if wine_overall != data.get('overall'):
                tz = pytz.timezone('Europe/London')
                now = datetime.now(tz)
                wine.posted_on = now
            wine.save()
            form.save_m2m()
            messages.success(request, data.get('name') + " has been edited successfully.")
            return redirect('show_messages')
        else:
            form = WineForm(instance=wine)
            messages.error(request, 'Wine was not saved')
            return redirect(request, "wineapp/add_wine.html")

    else:
        form = WineForm(instance=wine)
    return render(request, 'wineapp/add_wine.html', {'form': form})

def wine_details(request, id):

    wine = get_object_or_404(Wine, id=id)
    wine = Wine.objects.get(id=id)
    grapes = wine.grapes.all()
    style = str(wine.type)
    country = str(wine.country)
    total_likes = wine.like

    context = {
        'range': range(10),
        'wine': wine,
        'style': style,
        'country': country,
        'grapes': grapes,
        'total_likes': total_likes,
    }
    return render(request, "wineapp/wine_details.html", context)

def about(request, *args, **kwargs):

    about_wineapp = {
        "name": "Wine or Whine",
        "author": "Vinus de Wino",
        "email": "wineorwhine21@gmail.com",
        "disclaimer": "This is just my opinion on the wines " \
        "I have tried. Like all wine reviews, " \
        "they are subjective and my reviews should not influence " \
        "your wine buying options.",
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
        form = CustomUserCreationForm(request.GET or None)
        return render(
            request, "registration/login.html", {"form": form}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")

            if password1 == password2:
                try:
                    user= User.objects.get(username=username)
                    context= {'form': form, 'error':'The username you entered has already been taken. Please try another username.'}
                    return render(request, "registration/login.html", context)
                except User.DoesNotExist:
                    user= User.objects.create_user(username, password= password1, email=email)

                    user.save()
                    login(request, user)
                    return redirect(reverse("home"))
            else:
                 context= {'form': form, 'error':'The passwords that you provided don\'t match'}
                 return render(request, "registration/login.html", context)

            if email is None or '' :
                try:
                    user= User.objects.get(email=email)
                    context= {'form': form, 'error':'Email is required'}
                    return render(request, "registration/login.html", context)
                except User.DoesNotExist:
                   user= User.objects.create_user(username, password= password1, email=email)

                   user.save()
                   login(request, user)
                   return redirect(reverse("home"))
            else:
                 context= {'form': form, 'error':'Email does not meet the required details'}
                 return render(request, "registration/login.html", context)

        else:
             return render(request, "registration/login.html", {'form': form})

def like(request, pk):

    if request.method == "POST":
        user = request.user
        wine = get_object_or_404(Wine, id=request.POST.get('wine_id'))
        current_likes = wine.like
        liked = Likes.objects.filter(user=user, wine=wine).count()

        if not liked:
            like = Likes.objects.create(user=user, wine=wine)
            current_likes = current_likes + 1

        else:
            Likes.objects.filter(user=user, wine=wine).delete()
            current_likes =current_likes - 1

        wine.like = current_likes
        wine.save()

        return HttpResponseRedirect(reverse('wine_details', args=[str(pk)]))

def add_comment(request, id):
    wine = get_object_or_404(Wine, id=id)

    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.wine = wine
            comment.user = request.user
            comment.save()
            return redirect('wine_details', id=wine.id)
    else:
        form = CommentForm()
    return render(request, 'wineapp/add_comment.html', {'form': form})

def comment_approve(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.approve()
    return redirect('wine_details', id=comment.wine.id)

def comment_remove(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect('wine_details', id=comment.wine.id)

def show_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')
    Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)
    context = {
        'notifications': notifications,
    }

    return render(request, "wineapp/notifications.html", context)

def delete_notification(request, id):

    if request.method == "POST":
        user= request.user
        notification = Notification.objects.filter(id=id, user=user)
        notification.delete()
        return redirect('show_notifications')
    else:
        return redirect('show_notifications')

def count_notifications(request):
	count_notifications = 0
	if request.user.is_authenticated:
		count_notifications = Notification.objects.filter(user=request.user, is_seen=False).count()

	return {'count_notifications':count_notifications}
