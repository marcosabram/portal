from django.shortcuts import render
from django.views.generic.list import ListView
from Users.models import User
from django.views.generic.edit import UpdateView  
# Create your views here.

class AjaxableResponseMixin:

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

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

    def get_context_data(self, **kwargs):
        context=super(Usuarios,self).get_context_data(**kwargs)   
        context['tipos']=(('1','Lector'),('2','Editor'))
        return context

class ActualizarPermiso(AjaxableResponseMixin,UpdateView):
    model=User
    fields=['tipo']


