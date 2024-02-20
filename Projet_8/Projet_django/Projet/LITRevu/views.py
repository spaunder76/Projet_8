from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login


def index(request):
    context = {"message":"Hello world! "}
    template = loader.get_template("LITRevu/index.html")
    return HttpResponse(template.render(context, request))

def login_page(request):
    return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Rediriger l'utilisateur vers une page après la connexion réussie
            return redirect('nom_de_la_vue')
        else:
            # Gérer les erreurs de connexion
            # Par exemple, afficher un message d'erreur dans le template
            return render(request, 'index.html', {'erreur': 'Identifiants incorrects'})
    else:
        return render(request, 'index.html')
