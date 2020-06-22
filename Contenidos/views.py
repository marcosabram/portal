from django.shortcuts import render
from django.urls import reverse, reverse_lazy
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

class CrearDocumento(CreateView):
    model=Documento
    template_name='crear_contenido.html'
    success_url = reverse_lazy('index')
    fields=['titulo','texto','grupo']

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        #import pdb; pdb.set_trace()
         
        #kwargs.update({'data': self.object})
        return kwargs

class Contenido(TemplateView):
    template_name = 'contenido.html'


