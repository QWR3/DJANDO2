from django.contrib import admin

from phones.models import PhoneModel


@admin.register(PhoneModel)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'camera', 'RAM', 'CPU', 'diagonal', 'price']

