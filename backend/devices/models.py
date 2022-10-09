import uuid
import logging
from django.db import models
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)


# Create your models here.
class Device(models.Model):
    """This is the model for the Device"""
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='devices')
    uninstall_code = models.CharField(default=uuid.uuid4(), max_length=255)
    uuid = models.CharField(default=uuid.uuid4(), unique=True, max_length=255)
    name = models.CharField(max_length=100)
    registered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def verify_uninstall_code(self, code):
        """This function verifies the uninstall code"""
        return code == self.uninstall_code

    def __str__(self):
        return str(self.name)


class Screenshot(models.Model):
    """This is the model for the Screenshot"""
    device = models.ForeignKey(Device,
                               on_delete=models.CASCADE,
                               related_name='screenshots')
    false_positive = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device.name


GENERATED_UNINSTALL_CODE_MESSAGE = """
Hello {name},
Your chaver {email} has requested a code to uninstall the app from his device named {device_name}.
He can now uninstall the app from his device.

Best regards,
The OpenChaver team.
"""

UNINSTALL_MESSAGE = """
Hi {name},
You chaver {email} has uninstalled the OpenChaver app from his device named {device_name}.
You will no longer receive alerts or reports from this device.
If you wish to continue receiving alerts and reports from this device, please contact {email}.

Best regards,
The OpenChaver team.
"""

REMOVED_MESSAGE = """
Hi {name},
You have been removed as a chaver from the device named {device_name}.
You will no longer receive alerts or reports from this device.
If you wish to continue receiving alerts and reports from this device, please contact {email}.

Best regards,
The OpenChaver team.
"""


class Chaver(models.Model):
    """This is the model for the Chaver"""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    device = models.ForeignKey(Device,
                               on_delete=models.CASCADE,
                               related_name='chavers')
    created = models.DateTimeField(auto_now_add=True)

    def send_uninstall_code(self):
        """This function sends an email to the chaver to notify him that his chaver can uninstall the app"""
        self.send_email(
            subject='OpenChaver uninstall code',
            message=GENERATED_UNINSTALL_CODE_MESSAGE.format(
                name=self.name,
                email=self.email,
                device_name=self.device.name,
            ),
        )

    def send_uninstall_email(self):
        """This function sends an email to the chaver when the device is uninstalled"""
        self.send_email(
            subject='Alert: OpenChaver uninstalled',
            message=UNINSTALL_MESSAGE.format(
                name=self.name,
                email=self.email,
                device_name=self.device.name,
            ),
        )

    def send_chaver_removed_email(self):
        """This function sends an email to the chaver when he is removed from the device"""
        self.send_email(
            subject='Alert: You\'ve been removed',
            message=REMOVED_MESSAGE.format(
                name=self.name,
                email=self.email,
                device_name=self.device.name,
            ),
        )

    def send_email(self, subject, message, fail_silently=True):
        """This function sends an email to the chaver"""
        logger.info(f'Sending email to {self.email}')
        logger.debug(f'Subject: {subject}')
        logger.debug(f'Message: {message}')
        logger.debug(f'Fail silently: {fail_silently}')

        send_mail(
            subject,
            message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.email],
            fail_silently=fail_silently,
        )

    def __str__(self):
        return self.device.name
