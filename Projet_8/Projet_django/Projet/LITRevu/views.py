from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import TicketForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db import models
from .models import Critique
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import CritiqueForm 
from .models import UserProfile



def index(request):
    context = {"message": "Hello world!"}
    if request.user.is_authenticated:
        ticket_form = TicketForm()
        context['ticket_form'] = ticket_form
    return render(request, "LITRevu/index.html", context)


def login_page(request):
    return render(request, 'LITRevu/login.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('indexofLITRevu')
        else:
            return render(request, 'LITRevu/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'LITRevu/login.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('indexofLITRevu')
    else:
        form = UserCreationForm()
    return render(request, 'LITRevu/registration.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('indexofLITRevu')


def create_ticket(request):
    if request.method == 'POST':
        ...
        return redirect('indexofLITRevu')
    else:
        ticket_form = TicketForm()
        return render(request, 'LITRevu/create_ticket.html', {'ticket_form': ticket_form})


def liste_critiques(request):
    critiques = Critique.objects.all()
    return render(request, 'LITRevu/liste_critiques.html', {'critiques': critiques})


@login_required
def publier_critique(request):
    if request.method == 'POST':
        form = CritiqueForm(request.POST)
        if form.is_valid():
            critique = form.save(commit=False)
            critique.auteur = request.user
            critique.save()
            return redirect('indexofLITRevu')
    else:
        form = CritiqueForm()
    return render(request, 'LITRevu/publier_critique.html', {'form': form})

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    critiques = Critique.objects.filter(auteur=user)
    return render(request, 'LITRevu/user_profile.html', {'user': user, 'critiques': critiques})


@login_required
def list_following(request):
    profile = request.user.profile
    following_users = profile.following.all()
    return render(request, 'list_following.html', {'following_users': following_users})

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if user_to_follow != request.user:
        if user_to_follow not in profile.following.all():
            profile.following.add(user_to_follow)
    return redirect('user_profile', username=username)

@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=request.user)
    profile.following.remove(user_to_unfollow)
    return redirect('user_profile', username=username)







    

