"""Contains the serializers for the devices app."""
from rest_framework import serializers as s

from .models import Device, Screenshot, Chaver

class DeviceSerializer(s.ModelSerializer):
    """This is the serializer for the Device model"""
    class Meta: # pylint: disable=missing-class-docstring
        model = Device
        fields = ('id','user','name','device_id','created','registered','screenshots','chavers')
        read_only_fields = ('created','device_id','screenshots','chavers','id','registered','user')

class UninstallCodeSerializer(s.ModelSerializer):
    """Serializer for uninstall code"""
    class Meta: # pylint: disable=missing-class-docstring
        model = Device
        fields = ('uninstall_code',)
        read_only_fields = ('uninstall_code',)

class ScreenshotSerializer(s.ModelSerializer):
    """Serializer for the Screenshot model."""
    class Meta: # pylint: disable=missing-class-docstring
        model = Screenshot
        fields = ('id','device','image', 'created','nsfw','false_positive')

class ScreenshotUploadSerializer(s.Serializer):
    """Serializer for uploading the Screenshots."""
    device_id = s.CharField()
    image = s.ImageField()
    nsfw = s.BooleanField()
    false_positive = s.BooleanField()

class ChaverSerializer(s.ModelSerializer):
    """Serializer for the Chaver model."""
    class Meta: # pylint: disable=missing-class-docstring
        model = Chaver
        fields = ('id', 'name', 'email',"device", 'created')

class RegisterDeviceSerializer(s.Serializer):# pylint: disable=abstract-method
    """Serializer for registering a device"""
    device_id = s.CharField(max_length=100)

class VerifyUninstallCodeSerializer(s.Serializer):# pylint: disable=abstract-method
    """Serializer for verifying the uninstall code"""
    device_id = s.CharField(max_length=100)
    uninstall_code = s.CharField(max_length=100)
    
