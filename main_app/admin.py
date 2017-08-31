from django.contrib import admin

# Register your models here.
from .models import  Work
from .models import  School
from .models import  Person

admin.site.register(Work)
admin.site.register(School)
admin.site.register(Person)