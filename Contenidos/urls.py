from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from Contenidos import views

urlpatterns = [
    path(route='',
         view=views.Inicio.as_view(),
         name='index'),

    path(route='contenido/<pk>/',
         view=views.Contenido.as_view(),
         name='contenido'),
]
