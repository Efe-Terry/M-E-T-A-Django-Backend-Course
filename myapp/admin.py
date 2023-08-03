from django.contrib import admin
from .models import MenuCategory
from .models import Menu
from .models import Person
from .models import Customer
from .models import Vehicle
from .models import Logger
from .models import Reservation

# Register your models here.
admin.site.register(MenuCategory)
admin.site.register(Menu)
admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Logger)
admin.site.register(Reservation)

@admin.register(Person) 
class PersonAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True 

        return form

    list_display = ("last_name", "first_name") 
    search_fields = ("first_name__startswith", )