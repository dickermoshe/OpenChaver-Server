from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Device, Screenshot, Chaver, Log

@admin.action(description='Send reports for selected devices')
def send_reports(modeladmin, request, queryset):
    for device in queryset:
        device.send_report()

class DeviceAdmin(admin.ModelAdmin):
    actions = [send_reports]

admin.site.register(Device, DeviceAdmin)

class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ['title','device_html', 'nsfw', 'profane','created']
    list_filter = ['nsfw', 'profane']
    search_fields = ['title', 'device__name']

    def device_html(self, obj):
        return format_html('<a href="/admin/devices/device/{}/change/">{}</a>', obj.device.id, obj.device.name)

admin.site.register(Screenshot, ScreenshotAdmin)

admin.site.register(Chaver)
admin.site.register(Log)