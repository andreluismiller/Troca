from django.shortcuts import render
import folium 
from trocasolidaria.forms import CestaForm
from .models import *
import geocoder


def home(request):
    cestas = Cesta.objects.all()
    context = {'cestas': cestas}
    return render(request, 'trocasolidaria/home.html', context)


def form_cestaform(request):
    if request.method == 'GET':
        form = CestaForm()
        context = {'form': form}
        return render(request, 'trocasolidaria/formulario_cesta.html', context)
    else:
        form = CestaForm(request.POST)
        if form.is_valid():
            cesta = form.save()
            form = CestaForm()
            
        context = {'form': form}
        return render(request, 'trocasolidaria/home.html', context)

        #Criar objeto mapa
        """
        m = folium.Map()
        m = m._repr_html()
        context = { 'm': m, }
        """
def detalhecesta(request):
    location = geocoder.osm('BR')
    lat =location.lat
    lng = location.lng
    country = location.country
    m = folium.Map(location=[19, -12], zoom_start=2)
    folium.Marker([lat, lng], tooltip='Clique para mais', popup=country).add_to(m)
    m = m._repr_html_()
    context = { 'm': m, }
    return render(request, 'trocasolidaria/detalhes_cesta.html', context)