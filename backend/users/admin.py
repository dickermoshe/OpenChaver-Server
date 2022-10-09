"""This is the AppConfig for the users app. It is used to configure the app and its models."""
from django.contrib import admin

# Register your models here.
from users.models import CustomUser
admin.site.register(CustomUser)
