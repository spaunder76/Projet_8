from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexofLITRevu'),
    path('login/', views.login_page, name='login_page'),
    path('login_view/', views.login_view, name='login_view'),  
    path('registration/', views.registration, name='registration_page'),
    path('logout/', views.logout_view, name='logout'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),  
    path('liste_critiques/', views.liste_critiques, name='liste_critiques'),
    path('user_profile/<str:username>/', views.user_profile, name='user_profile'),
    path('follow_user/<str:username>/', views.follow_user, name='follow_user'),
    path('unfollow_user/<str:username>/', views.unfollow_user, name='unfollow_user'),
    path('publier_critique/', views.publier_critique, name='publier_critique'),
    path('follow/', views.follow_user, name='follow_user'),
    path('following/', views.list_following, name='list_following'),
]

