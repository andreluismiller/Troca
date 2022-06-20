from django.shortcuts import render
from .models import *

def home(request):
    cestas = Cesta.objects.all()
    context = {'cestas': cestas}
    return render(request, 'trocasolidaria/home.html', context)
