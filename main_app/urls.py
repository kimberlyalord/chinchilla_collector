from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chinchillas/', views.ChinchillaList.as_view(), name='index'),
    path('chinchillas/<int:chinchilla_id>/', views.chinchillas_detail, name='detail'),
    path('chinchillas/create/', views.ChinchillaCreate.as_view(), name='chinchillas_create'),
    path('chinchillas/<int:pk>/update/', views.ChinchillaUpdate.as_view(), name='chinchillas_update'),
    path('chinchillas/<int:pk>/delete/', views.ChinchillaDelete.as_view(), name='chinchillas_delete'),
    path('chinchillas/<int:chinchilla_id>/add_bath/', views.add_bath, name='add_bath'),
    path('chinchillas/<int:chinchilla_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('chinchillas/<int:chinchilla_id>/add_photo/', views.add_photo, name='add_photo'),
    path('chinchillas/<int:chinchilla_id>/add_toy/<int:toy_id>/', views.add_toy, name='add_toy'),
    path('chinchillas/<int:chinchilla_id>/remove_toy/<int:toy_id>/', views.remove_toy, name='remove_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]