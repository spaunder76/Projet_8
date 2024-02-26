from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout


def index(request):
    context = {"message":"Hello world! "}
    template = loader.get_template("LITRevu/index.html")
    return HttpResponse(template.render(context, request))

def login_page(request):
    return render(request, 'LITRevu/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('indexofLITRevu')
        else:
            return redirect('indexofLITRevu')
    else:
        return render(request, 'LITRevu/login.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Vérifier si les mots de passe correspondent
        if password1 == password2:
            # Vérifier si l'utilisateur n'existe pas déjà
            if not User.objects.filter(username=username).exists():
                # Créer un nouvel utilisateur
                user = User.objects.create_user(username=username, email=email, password=password1)
                # Connecter l'utilisateur immédiatement après son inscription
                login(request, user)
                return redirect('indexofLITRevu')  # Rediriger vers la page d'accueil après l'inscription
            else:
                return render(request, 'LITRevu/registration.html', {'error': 'Cet utilisateur existe déjà'})
        else:
            return render(request, 'LITRevu/registration.html', {'error': 'Les mots de passe ne correspondent pas'})

    return render(request, 'LITRevu/registration.html')

def logout_view(request):
    logout(request)
    return redirect('indexofLITRevu')
