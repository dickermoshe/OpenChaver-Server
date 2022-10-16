from django.contrib import admin

# Register your models here.
from .models import Device, Screenshot, Chaver, Log

@admin.action(description='Send reports for selected devices')
def send_reports(modeladmin, request, queryset):
    for device in queryset:
        device.send_report()

class DeviceAdmin(admin.ModelAdmin):
    actions = [send_reports]

admin.site.register(Device, DeviceAdmin)
admin.site.register(Screenshot)
admin.site.register(Chaver)
admin.site.register(Log)