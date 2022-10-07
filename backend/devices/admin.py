from django.contrib import admin

# Register your models here.
from .models import Device, Screenshot, Chaver

admin.site.register(Device)
admin.site.register(Screenshot)
admin.site.register(Chaver)

