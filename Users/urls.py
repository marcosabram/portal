from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from Users import views

urlpatterns = [
    path(route='usuarios/',
        view=views.Usuarios.as_view(),
        name='usuarios'),

    path(route='usuarios/<pk>/editar/',
        view=views.ActualizarPermiso.as_view(),
        name='editar_usuario'), 
]