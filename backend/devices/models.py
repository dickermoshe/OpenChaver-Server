import uuid
from django.db import models
from django.contrib.auth import get_user_model

def get_random_code():
    code = str(uuid.uuid4())[:8].replace('-', '').lower()
    return code

# Create your models here.
class Device(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='devices')
    uninstall_code = models.CharField(max_length=8, default=get_random_code)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Screenshot(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='screenshots')
    false_positive = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device.name

class Chaver(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='chavers')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device.name
    
