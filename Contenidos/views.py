from django.shortcuts import render
from django.views.generic.edit import View
from django.views.generic import TemplateView


# Create your views here.

class Inicio(TemplateView):
    template_name = 'cards.html'

class Contenido(TemplateView):
    template_name = 'contenido.html'


