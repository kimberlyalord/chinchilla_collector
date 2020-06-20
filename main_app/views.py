from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Chinchilla, Toy, Photo
from .forms import BathForm, FeedingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollector-sei-cc-8'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def chinchillas_detail(request, chinchilla_id):
    chinchilla = Chinchilla.objects.get(id=chinchilla_id)
    toys_available = Toy.objects.exclude(id__in = chinchilla.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    bath_form = BathForm()
    return render(request, 'chinchillas/detail.html', {
        'chinchilla': chinchilla,
        'feeding_form': feeding_form,
        'bath_form': bath_form,
        'toys': toys_available,
    })

class ChinchillaList(LoginRequiredMixin, ListView):
    model = Chinchilla
    # queryset = Chinchilla.objects.filter(chinchilla.user=)
    
class ChinchillaCreate(LoginRequiredMixin, CreateView):
    model = Chinchilla
    fields = ['name', 'color', 'description', 'age']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ChinchillaUpdate(LoginRequiredMixin, UpdateView):
    model = Chinchilla
    fields = ['color', 'description', 'age']
    
class ChinchillaDelete(LoginRequiredMixin, DeleteView):
    model = Chinchilla
    success_url = '/chinchillas/'

@login_required 
def add_bath(request, chinchilla_id):
    form = BathForm(request.POST)
    if form.is_valid():
        new_bath = form.save(commit=False)
        new_bath.chinchilla_id = chinchilla_id
        new_bath.save()
    return redirect('detail', chinchilla_id=chinchilla_id)

@login_required
def add_feeding(request, chinchilla_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.chinchilla_id = chinchilla_id
        new_feeding.save()
    return redirect('detail', chinchilla_id=chinchilla_id)

@login_required
def add_photo(request, chinchilla_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, chinchilla_id=chinchilla_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', chinchilla_id=chinchilla_id)

class ToyList(LoginRequiredMixin, ListView):
    model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'

@login_required
def add_toy(request, chinchilla_id, toy_id):
    Chinchilla.objects.get(id=chinchilla_id).toys.add(toy_id)
    return redirect('detail', chinchilla_id=chinchilla_id)

@login_required
def remove_toy(request, chinchilla_id, toy_id):
    Chinchilla.objects.get(id=chinchilla_id).toys.remove(toy_id)
    return redirect('detail', chinchilla_id=chinchilla_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again!'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)