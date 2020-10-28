from django.contrib import admin
from .models import Person, PointOfInterest
# Register your models here.
admin.site.register(Person)
admin.site.register(PointOfInterest)
