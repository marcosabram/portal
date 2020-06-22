from django.shortcuts import render
from django.views.generic.edit import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView    
from Contenidos.models import Documento

# Create your views here.

class Inicio(ListView):#lista todos los contenidos
    model=Documento
    context_object_name='documentos'
    template_name='cards.html'
    paginate_by=10
    ordering=['-modified_date']


class Contenido(TemplateView):
    template_name = 'contenido.html'


class EditarContenido(UpdateView):
    model = Documento
    context_object_name='documentos'
    template_name='crear_contenido.html'





