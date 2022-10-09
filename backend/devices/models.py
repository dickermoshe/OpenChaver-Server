import uuid
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Device(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='devices')
    uuid = models.CharField(default=uuid.uuid4(), unique=True,max_length=255)
    uninstall_code = models.CharField(null=True, blank=True, max_length=255)
    name = models.CharField(max_length=100)
    registered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def latest_screenshot(self):
        try:
            return self.screenshots.order_by('-created').first().created
        except:
            return None
    
    def get_uninstall_code(self):
        self.uninstall_code = uuid.uuid4()
        self.save()
        return self.uninstall_code
    
    def verify_uninstall_code(self, code):
        return code == self.uninstall_code


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
    
