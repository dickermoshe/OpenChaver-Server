"""Contains the serializers for the devices app."""
from random import randint
import string
from uuid import uuid4
from rest_framework import serializers as s
import base64
import numpy as np
import cv2
from PIL import Image
from io import BytesIO

# IMport Django File
from django.core.files.base import ContentFile

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

def deobfuscate_text(text:str):
    # From Openchaver/models.py
    a = string.ascii_letters
    b = string.ascii_letters[-1] + string.ascii_letters[:-1]
    table = str.maketrans(b, a)
    return text.translate(table)

def decode_base64_to_numpy(img: str) -> np.ndarray:
    # From Openchaver/image_utils/encoders.py
    """
    Decode a base64 string to a numpy array.
    """
    return cv2.imdecode(np.frombuffer(base64.b64decode(img), np.uint8), -1)

class ScreenshotUploadSerializer(s.Serializer):
    """Serializer for uploading the Screenshots."""
    title = s.CharField()
    exec_name = s.CharField()
    base64_image = s.CharField(trim_whitespace=False) # Base64 

    nsfw = s.BooleanField(default=False)
    profane = s.BooleanField(default=False)

    nsfw_detections = s.JSONField(default=dict)
    created = s.DateTimeField()

    false_positive = s.BooleanField(default=False)

    device_id = s.UUIDField()

    def create(self, validated_data):
        """Create a new screenshot."""
        device_id = validated_data.pop('device_id')
        device = Device.objects.get(device_id=device_id)
        
        # DeObfuscate the title and exec_name
        title = validated_data.pop('title')
        exec_name = validated_data.pop('exec_name')
        title = deobfuscate_text(title)
        exec_name = deobfuscate_text(exec_name)

        # Decode the base64 image to a numpy array
        base64_image = validated_data.pop('base64_image')
        img_arr = decode_base64_to_numpy(base64_image)
        
        # Convert the numpy array to a PIL image
        img = Image.fromarray(img_arr)
        
        # Save the image to a BytesIO object
        img_io = BytesIO()
        img.save(img_io, format='PNG')

        file = ContentFile(img_io.getvalue(), name=uuid4().hex + '.png')
        
        # Create the screenshot
        screenshot = Screenshot.objects.create(
            title=title,
            exec_name=exec_name,
            image=file,
            device=device,
            **validated_data
        )
        return screenshot

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
    
