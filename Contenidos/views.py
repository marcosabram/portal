from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView    
from Users.models import User
from Contenidos.models import Documento
from django.contrib.auth.models import Group

# Create your views here.

class Inicio(ListView):#lista todos los contenidos
    model=Documento
    context_object_name='documentos'
    template_name='cards.html'
    paginate_by=10
    ordering=['-modified_date']

    def get_queryset(self):
        user=self.request.user
        grupoID=user.groups.get().id
        self.queryset=Documento.objects.filter(grupo=grupoID,aprobado=True)
        return super().get_queryset()

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

    def form_valid(self, form):
        response = super().form_valid(form)
        user=self.request.user
        grupoID=user.groups.get().id
        if user.is_staff==False:
            adminGrupo=User.objects.get(is_staff=True,groups__id=grupoID)
            mensaje= user.get_full_name() + ' a creado una nueva publicacion.'
            adminGrupo.email_user('Nueva Publicacion', mensaje, from_email=None)
        return response


class EditarContenido(UpdateView):
    model = Documento
    context_object_name='documento'
    template_name='crear_contenido.html'
    fields = ['titulo','texto']
    success_url = reverse_lazy('contenidos:index')

class EliminarDocumento(DeleteView):
    model=Documento
    success_url = reverse_lazy('contenidos:index')
    template_name='documento_confirm_delete.html'

class DocumentosPendientes(ListView):#lista todos los contenidos
    model=Documento
    context_object_name='documentos'
    template_name='cards.html'
    paginate_by=10
    ordering=['-modified_date']

    def get_queryset(self):
        user=self.request.user
        grupoID=user.groups.get().id
        self.queryset=Documento.objects.filter(grupo=grupoID,aprobado=False)
        return super().get_queryset()

class AprobarDocumento(UpdateView):
    model = Documento
    context_object_name='documento'
    template_name='aprobar_contenido.html'
    fields = ['aprobado']
    success_url = reverse_lazy('contenidos:documentos_pendientes')



