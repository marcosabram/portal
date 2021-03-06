from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.
class User(AbstractUser):
    
    SELECT_TIPO = (('1','Lector'),('2','Editor'))      
    tipo = models.CharField('Tipo de usuario',max_length=20, choices=SELECT_TIPO,default='1')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email' , 'last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('contenidos:index')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'