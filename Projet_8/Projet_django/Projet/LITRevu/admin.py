from django.contrib import admin
from .models import Ticket, Review, Critique

admin.site.register(Ticket)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','created_at') 
    search_fields = ('title', 'description') 

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'rating', 'headline', 'user', 'time_created')
    search_fields = ('headline', 'user__username')  # Recherche par nom d'utilisateur
    list_filter = ('rating',)  # Filtre par note

# Enregistrer le modèle Review avec sa classe d'administration personnalisée
admin.site.register(Review, ReviewAdmin)

# Enregistrer le modèle Critique
class CritiqueAdmin(admin.ModelAdmin):
    list_display = ('titre', 'contenu', 'auteur', 'date_creation')
    search_fields = ('titre', 'auteur__username')  # Recherche par nom d'utilisateur
    list_filter = ('date_creation',)  # Filtre par date de création

# Enregistrer le modèle Critique avec sa classe d'administration personnalisée
admin.site.register(Critique, CritiqueAdmin)