from django.db import models

class Customer(models.Model): 
    name = models.CharField(max_length=255) 

class Vehicle(models.Model): 
    name = models.CharField(max_length=255) 
    customer = models.ForeignKey( 
        Customer, 
        on_delete=models.CASCADE, 
        related_name='Vehicle' 
    ) 

class RstCustomers(models.Model):
    name = models.CharField(max_length=30)
    reservation_day = models.CharField(max_length=50)
    seat_number = models.IntegerField()