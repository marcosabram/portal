from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from Contenidos import views

urlpatterns = [
    path(route='',
         view=views.Inicio.as_view(),
         name='index'),

     path(route='documentos/add',
         view=views.CrearDocumento.as_view(),
         name='crear_documento'),

    path(route='documentos/<pk>/editar',
         view=views.EditarContenido.as_view(),
         name='editar_contenido'),
         
    path(route='documentos/<pk>/eliminar',
         view=views.EliminarDocumento.as_view(),
         name='eliminar_documento'),

     path(route='documentos/pendientes',
         view=views.DocumentosPendientes.as_view(),
         name='documentos_pendientes'), 

     path(route='documentos/pendientes/<pk>/editar',
         view=views.AprobarDocumento.as_view(),
         name='aprobar_documento'),       
]
