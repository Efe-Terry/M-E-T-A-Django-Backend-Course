from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('myapp.urls')),
    path('alx/', include('alx.urls')),
]

handler404 = 'meta.views.handler404'