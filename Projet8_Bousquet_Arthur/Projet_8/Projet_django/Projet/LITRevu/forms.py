from django import forms
from .models import Critique


class TicketForm(forms.Form):
    title = forms.CharField(max_length=100, label='Titre du ticket')
    description = forms.CharField(widget=forms.Textarea, label='Description du ticket')

class CritiqueForm(forms.ModelForm):
    class Meta:
        model = Critique
        fields = ['titre', 'contenu']

