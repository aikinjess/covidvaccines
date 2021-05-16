from django.contrib import admin
from .models import Patient, Dose

# Register your models here.

admin.site.register(Patient)
admin.site.register(Dose)