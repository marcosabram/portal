from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    SELECT_TIPO = (('1','Lector'),('2','Editor'))      
    tipo = models.CharField('Tipo de usuario',max_length=20, choices=SELECT_TIPO)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'