from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='home'),
     path('cadastrocesta/', view=views.form_cestaform, name='form_cestaform'),
     path('detalhecesta/', views.detalhecesta, name='detalhes-cesta')
]