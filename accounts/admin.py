from django.contrib import admin
from .models import Donator, Address, Volunteer

# Register your models here.
admin.site.register(Donator)
admin.site.register(Volunteer)
admin.site.register(Address)
