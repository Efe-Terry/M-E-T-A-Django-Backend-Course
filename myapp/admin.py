from django.contrib import admin
from .models import MenuCategory
from .models import Menu
from .models import Person
from .models import Customer
from .models import Vehicle

# Register your models here.
admin.site.register(MenuCategory)
admin.site.register(Menu)
admin.site.register(Person)
admin.site.register(Customer)
admin.site.register(Vehicle)
