from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexofLITRevu'),
    path('login/', views.login_page, name='login_page'),  # Garder celui-ci pour afficher la page de connexion
    path('login_view/', views.login_view, name='login_view'),  # Changer le nom de celui-ci pour éviter le conflit
    path('registration/', views.registration, name='registration_page'),
    path('logout/', views.logout_view, name='logout'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),  # Ajoutez ce chemin d'URL
    path('liste_critiques/', views.liste_critiques, name='liste_critiques'),
    path('publier_critique/', views.publier_critique, name='publier_critique'),
]

