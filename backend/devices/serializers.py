"""Contains the serializers for the devices app."""
from rest_framework import serializers as s

from .models import Device, Screenshot, Chaver, Log


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
    title = s.CharField()
    exec_name = s.CharField()
    base64_image = s.CharField(trim_whitespace=False) # Base64 

    nsfw = s.BooleanField(default=False)
    profane = s.BooleanField(default=False)

    nsfw_detections = s.JSONField(default=dict)
    created = s.DateTimeField()

    false_positive = s.BooleanField(default=False)

    def create(self, validated_data, device):
        """Create a new screenshot."""
        from .utils import decode_base64_to_numpy, numpy_to_content_file,deobfuscate_text
        
        # DeObfuscate the title and exec_name
        title = validated_data.pop('title')
        exec_name = validated_data.pop('exec_name')
        title = deobfuscate_text(title)
        exec_name = deobfuscate_text(exec_name)

        # Decode the base64 image
        base64_image = validated_data.pop('base64_image')
        image = decode_base64_to_numpy(base64_image)
        file = numpy_to_content_file(image)

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

class VerifyUninstallCodeSerializer(s.Serializer):# pylint: disable=abstract-method
    """Serializer for verifying the uninstall code"""
    uninstall_code = s.CharField(max_length=100)

class DeviceSerializer(s.ModelSerializer):
    """This is the serializer for the Device model"""
    user = s.HiddenField(default=s.CurrentUserDefault())

    chavers = ChaverSerializer(many=True, read_only=True)
    screenshots = ScreenshotSerializer(many=True, read_only=True)

    class Meta: # pylint: disable=missing-class-docstring
        model = Device
        fields = ('id','user','name','created','registered','screenshots','chavers')
        read_only_fields = ('created','screenshots','chavers','id','registered','user')

    