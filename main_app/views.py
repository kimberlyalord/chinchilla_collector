from django.shortcuts import render, redirect
from .models import Chinchilla
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def chinchillas_detail(request, chinchilla_id):
    chinchilla = Chinchilla.objects.get(id=chinchilla_id)
    return render(request, 'chinchillas/detail.html', {
        'chinchilla': chinchilla,
    })

class ChinchillaList(ListView):
    model = Chinchilla
    
