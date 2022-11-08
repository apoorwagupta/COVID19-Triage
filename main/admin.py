from django.contrib import admin
from .models import *#importing patient, bed and doctor class from models.py
# Register your models here(with the admin site)
admin.site.register(Patient) # registering our models with admin.
admin.site.register(Bed)
admin.site.register(Doctor)