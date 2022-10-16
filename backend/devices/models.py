import uuid
import logging
from datetime import datetime, timedelta
from django.utils import timezone
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
    uninstall_code = models.CharField(default=uuid.uuid4, max_length=255)
    device_id = models.CharField(default=uuid.uuid4, max_length=255,unique=True,db_index=True)
    name = models.CharField(max_length=100)
    registered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def verify_uninstall_code(self, code):
        """This function verifies the uninstall code"""
        return code == self.uninstall_code
    
    def send_report(self):
        """
        This function sends a report to the user and all the chavers
        params:
            ids: list of ids of the screenshots to send
        """
        # Get screenshots from last 48 hours
        screenshots = self.screenshots.filter(created__gte=timezone.now() - timedelta(hours=48))
        
        # Get screenshots that are nsfw and are 72 hours old
        nsfw_screenshots = screenshots.filter(nsfw=True, created__lte=timezone.now() - timedelta(hours=72))

        # Combine the screenshots and nsfw_screenshots
        screenshots = screenshots | nsfw_screenshots
        
        tos = [self.user.email] + [chaver.email for chaver in self.chavers.all()]
        subject = f"Report for {self.name}"
        html_message = self.screenshots.model.create_report(screenshots)

        if self.registered is None or html_message is None:
            return

        send_mail(subject,
                    '',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=tos,
                    html_message=html_message,
                    fail_silently=True)

        



        


        
        

    def __str__(self):
        return str(self.name)


class Screenshot(models.Model):
    """This is the model for the Screenshot"""
    device = models.ForeignKey(Device,
                               on_delete=models.CASCADE,
                               related_name='screenshots')

    

    title = models.TextField()
    exec_name = models.TextField()

    image = models.ImageField(upload_to='images/', blank=True, null=True)

    nsfw = models.BooleanField(default=False)
    profane = models.BooleanField(default=False)

    nsfw_detections = models.JSONField(default=dict)
    created = models.DateTimeField()

    false_positive = models.BooleanField(default=False)
    

    def __str__(self):
        return self.device.name
    
    @classmethod
    def create_report(cls,screenshots:list["Screenshot"]):
        """This function creates a report for the screenshots"""
        if not screenshots:
            return
        
        # Create the report in raw html - Include the images and the title
        html = f"""
        <html>
            <head>
                <style>
                    table {{
                        border-collapse: collapse;
                    }}
                    table, th, td {{    
                        border: 1px solid black;
                    }}
                </style>
            </head>
            <body>
                <h1>Report for {screenshots[0].device.name}</h1>
                <table>
                    <tr>
                        <th>Title</th>
                        <th>Exec Name</th>
                        <th>NSFW</th>
                        <th>Profane</th>
                        <th>False Positive</th>
                        <th>Image</th>
                    </tr>
        """
        for screenshot in screenshots:
            html += f"""
                    <tr>
                        <td>{screenshot.title}</td>
                        <td>{screenshot.exec_name}</td>
                        <td>{screenshot.nsfw}</td>
                        <td>{screenshot.profane}</td>
                        <td>{screenshot.false_positive}</td>
                        <td><img src="{screenshot.image.url if screenshot.image else ""}" height="200"></td>
                    </tr>
            """
        html += """
                </table>
            </body>
        </html>
        """
        return html

        
        


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

class Log(models.Model):
    """This is the model for the Logs"""
    device = models.ForeignKey(Device,
                                 on_delete=models.CASCADE,
                                    related_name='logs')
                                    
    created = models.DateTimeField(auto_now_add=True)
    log = models.TextField()

    def __str__(self):
        return self.device.name
