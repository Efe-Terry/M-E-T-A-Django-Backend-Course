from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu),
    path('about/', views.about),
    path('name/', views.name),
    path('index/', views.index),
]