from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import TicketForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db import models
from .models import Critique





def index(request):
    context = {"message": "Hello world!"}
    if request.user.is_authenticated:
        # Si l'utilisateur est authentifié, instanciez le formulaire de ticket
        ticket_form = TicketForm()
        context['ticket_form'] = ticket_form

    return render(request, "LITRevu/index.html", context)


def login_page(request):
    return render(request, 'LITRevu/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Rediriger l'utilisateur vers la page d'accueil après la connexion réussie
            return redirect('indexofLITRevu')
        else:
            # Gérer les erreurs de connexion
            # Par exemple, afficher un message d'erreur dans le template
            return render(request, 'LITRevu/login.html', {'erreur': 'Identifiants incorrects'})
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

def create_ticket(request):
    if request.method == 'POST':
        # Traitement de la soumission du formulaire de ticket
        ...
        return redirect('indexofLITRevu')  # Rediriger vers la page d'index après la création du ticket
    else:
        ticket_form = TicketForm()  # Instancier le formulaire de ticket
        return render(request, 'LITRevu/create_ticket.html', {'ticket_form': ticket_form})
    
# Modèle pour le suivi des utilisateurs
class UserFollow(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

def liste_critiques(request):
    critiques = Critique.objects.all()
    return render(request, 'LITRevu/liste_critiques.html', {'critiques': critiques})

@login_required
def publier_critique(request):
    if request.method == 'POST':
        # Traitement de la soumission du formulaire de publication de critique
        # Assurez-vous de valider et de sauvegarder les données du formulaire correctement
        ...
        return redirect('indexofLITRevu')  # Rediriger vers la page d'index après la publication de la critique
    else:
        return render(request, 'LITRevu/publier_critique.html')




    

