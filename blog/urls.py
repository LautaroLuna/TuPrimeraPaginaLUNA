from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevo_autor/', views.nuevo_autor, name='nuevo_autor'),
    path('nueva_categoria/', views.nueva_categoria, name='nueva_categoria'),
    path('nuevo_post/', views.nuevo_post, name='nuevo_post'),
    path('buscar_post/', views.buscar_post, name='buscar_post'),

]
