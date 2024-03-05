from django import forms

class TicketForm(forms.Form):
    title = forms.CharField(max_length=100, label='Titre du ticket')
    description = forms.CharField(widget=forms.Textarea, label='Description du ticket')
    # Vous pouvez ajouter d'autres champs nécessaires pour votre ticket
