"""This is the AppConfig for the users app. It is used to configure the app and its models."""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Users app config."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
