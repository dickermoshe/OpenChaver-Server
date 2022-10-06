import uuid

from django.db import models

def get_random_code():
    code = str(uuid.uuid4())[:8].replace('-', '').lower()
    return code

# Create your models here.
class Device(models.Model):
    uuid = models.UUIDField(editable=False,default = uuid.uuid4,)
    uninstall_code = models.CharField(max_length=8, default=get_random_code)

    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Screenshot(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device.name
    
