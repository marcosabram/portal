from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('Contenidos.urls','contenidos'), namespace='contenidos')),
   # path('contenidos/documentos/create',)
]
