from unicodedata import name
from django.db import models

class Person(models.Model): 
    person_name = models.CharField(max_length=100)
    email = models.EmailField() 
    phone = models.CharField(max_length=100) 

    def __str__(self):
        return f'name -> {self.person_name} : email -> {self.email} : price -> {self.phone}'


class Menu(models.Model):
    name = models.CharField(max_length = 100)
    cuisine = models.CharField(max_length = 100)
    price = models.IntegerField()

    def __str__(self):
        return f'name -> {self.name} : cuisine -> {self.cuisine} : price -> {self.price}'

