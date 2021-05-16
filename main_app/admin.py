from django.contrib import admin
from .models import Patient, Dose, SideEffect

# Register your models here.

admin.site.register(Patient)
admin.site.register(Dose)
admin.site.register(SideEffect)