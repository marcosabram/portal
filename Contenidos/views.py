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

<<<<<<< HEAD
=======
class CrearDocumento(CreateView):
    model=Documento
    template_name='crear_contenido.html'
    success_url = reverse_lazy('contenidos:index')
    fields=['titulo','texto','grupo']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user=self.request.user
        context['grupo']=user.groups.get().id
        return context
     
>>>>>>> 5a1eb588b04510ae4a4e74b9b65ea98fe5009c17

class Contenido(TemplateView):
    template_name = 'contenido.html'


class EditarContenido(UpdateView):
    model = Documento
    context_object_name='documentos'
    template_name='crear_contenido.html'





