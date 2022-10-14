from .models import Device

def send_reports():
    """This function runs every 48 hours and sends a report to all the chavers"""
    devices = Device.objects.filter(registered=True)
    for device in devices:
        device.send_report()