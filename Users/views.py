from django.shortcuts import render
from django.views.generic.list import ListView
from Users.models import User
# Create your views here.
class Usuarios(ListView):#lista todos los contenidos
    model=User
    context_object_name='usuarios'
    template_name='usuarios.html'
    paginate_by=10
    ordering=['-last_name']

    def get_queryset(self):
        user=self.request.user
        grupoID=user.groups.get().id
        #import pdb; pdb.set_trace()
        self.queryset=User.objects.filter(groups=grupoID)
        return super().get_queryset()