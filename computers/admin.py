from django.contrib import admin

# Register your models here.
from computers.models import ComputerModel


@admin.register(ComputerModel)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ['id', 'CPU', 'memory', 'storage']
