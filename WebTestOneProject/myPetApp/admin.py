from django.contrib import admin
from.models import Pet

# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    # note pass is just a holder for now
    list_display = ['name', 'species', 'breed','sex']

