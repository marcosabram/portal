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
]
