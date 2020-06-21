from django.contrib import admin
from .models import Documento #importamos el modelo  
# Register your models here.

class DocumentosAdmin(admin.ModelAdmin):
    search_fields = ['created_date']

admin.site.register(Documento,DocumentosAdmin)#lo registramos en el admin de django