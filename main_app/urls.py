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

]