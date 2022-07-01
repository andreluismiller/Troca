from django import forms
from .models import Cesta
from django.forms import ModelForm

"""
Formulário para cadastro de cesta
"""

class CestaForm(forms.ModelForm):
    class Meta:
        model = Cesta
        fields = '__all__'

