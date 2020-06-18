from django.shortcuts import render, redirect
from .models import Chinchilla
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def chinchillas_index(request):
#     chinchillas = Chinchilla.objects.order_by('-id')
#     return render(request, 'chinchillas/index.html', {'chinchillas': chinchillas})

class ChinchillaList(ListView):
    model = Chinchilla
    
class ChinchillaDetail(DetailView):
    model = Chinchilla

