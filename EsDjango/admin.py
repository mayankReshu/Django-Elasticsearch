from django.contrib import admin

# Register your models here.
from .models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    class Meta:
        model = Person




admin.site.register(Person, PersonAdmin)
