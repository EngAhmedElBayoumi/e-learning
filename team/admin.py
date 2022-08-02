from atexit import register
from django.contrib import admin
from .models import teams,Reservation
# Register your models here.

admin.site.register(teams)
admin.site.register(Reservation)
