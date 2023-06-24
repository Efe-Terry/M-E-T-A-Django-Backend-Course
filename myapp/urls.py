from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('getuser/<name>/<id>/<cnt>', views.pathview, name='path'),
    path('getuser/', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"),
    path("getform/", views.getform, name='getform'),
    path("coffe/<str:name>", views.coffe, name="coffe"),
]