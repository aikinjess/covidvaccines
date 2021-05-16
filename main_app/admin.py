from django.contrib import admin
from .models import Patient, Dose, Vaccine, Photo

# Register your models here.

admin.site.register(Patient)
admin.site.register(Dose)
admin.site.register(Vaccine)
admin.site.register(Photo)