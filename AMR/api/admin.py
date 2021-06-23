from django.contrib import admin

# Register your models here.
from .models import  Vender, DeviceModel
admin.site.register(Vender)
admin.site.register(DeviceModel)
