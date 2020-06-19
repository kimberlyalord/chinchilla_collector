from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Chinchilla, Toy
from .forms import BathForm, FeedingForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def chinchillas_detail(request, chinchilla_id):
    chinchilla = Chinchilla.objects.get(id=chinchilla_id)
    feeding_form = FeedingForm()
    bath_form = BathForm()
    return render(request, 'chinchillas/detail.html', {
        'chinchilla': chinchilla,
        'feeding_form': feeding_form,
        'bath_form': bath_form,
    })

class ChinchillaList(ListView):
    model = Chinchilla
    
class ChinchillaCreate(CreateView):
    model = Chinchilla
    fields = '__all__'
    
class ChinchillaUpdate(UpdateView):
    model = Chinchilla
    fields = ['color', 'description', 'age']
    
class ChinchillaDelete(DeleteView):
    model = Chinchilla
    success_url = '/chinchillas/'
    
def add_bath(request, chinchilla_id):
    form = BathForm(request.POST)
    if form.is_valid():
        new_bath = form.save(commit=False)
        new_bath.chinchilla_id = chinchilla_id
        new_bath.save()
    return redirect('detail', chinchilla_id=chinchilla_id)
    
def add_feeding(request, chinchilla_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.chinchilla_id = chinchilla_id
        new_feeding.save()
    return redirect('detail', chinchilla_id=chinchilla_id)

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'
    
def add_toy(request, chinchilla_id, toy_id):
    Chinchilla.objects.get(id=chinchilla_id).toys.add(toy_id)
    return redirect('detail', chinchilla_id=chinchilla_id)

def remove_toy(request, chinchilla_id, toy_id):
    Chinchilla.objects.get(id=chinchilla_id).toys.remove(toy_id)
    return redirect('detail', chinchilla_id=chinchilla_id)