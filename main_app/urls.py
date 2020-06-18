from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chinchillas/', views.ChinchillaList.as_view(), name='index'),
]