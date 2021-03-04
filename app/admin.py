from django.contrib import admin
from .models import Labreport


class LabreportAdmin(admin.ModelAdmin): 
    list_display = ('Lab_Number', 'report') 
# Register your models here.
admin.site.register(Labreport,LabreportAdmin)