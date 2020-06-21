from django.shortcuts import render
from django.views.generic.edit import View

# Create your views here.
class Inicio(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cards.html')

