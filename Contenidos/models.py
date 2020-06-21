from django.db import models
from django.contrib.auth.models import Group

# Create your models here.

class Documento(models.Model):
    grupo=models.ForeignKey(Group,on_delete=models.CASCADE) # cada documento pertenece a un grupo, no a un usuario
    titulo=models.CharField(max_length=140)
    texto=models.CharField(max_length=5000,null=True)#por defecto es null
    created_date = models.DateTimeField(('Date created'), auto_now_add=True)
    modified_date = models.DateTimeField(('Date modified'), auto_now=True)

    def __str__(self): #alias que identifica describe al objeto
        return self.titulo

