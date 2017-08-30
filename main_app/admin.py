from django.contrib import admin

# Register your models here.
from .models import  Work
from .models import  School

admin.site.register(Work)
admin.site.register(School)