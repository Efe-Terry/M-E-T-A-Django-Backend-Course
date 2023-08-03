from unicodedata import name
from django.db import models

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    #price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT)

    def __str__(self):
        return f'menu-items -> {self.menu_item}'

class Customer(models.Model): 
    name = models.CharField(max_length=255) 

class Vehicle(models.Model): 
    name = models.CharField(max_length=255) 
    customer = models.ForeignKey( 
        Customer, 
        on_delete=models.CASCADE, 
        related_name='Vehicle' 
    ) 
'''
class Person(models.Model): 
    person_name = models.CharField(max_length=100)
    #email = models.EmailField() 
    phone = models.CharField(max_length=100) 

    def __str__(self):
        return f'name -> {self.person_name} : price -> {self.phone}'
'''
class Person(models.Model): 
    last_name = models.CharField(max_length=200, default="last_name")
    first_name = models.CharField(max_length=200, default="first_name")

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.DateTimeField('Enter Reservation Time')

class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone Number', max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.name}"