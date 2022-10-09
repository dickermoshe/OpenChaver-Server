from rest_framework import serializers as s

from .models import Device, Screenshot, Chaver

class DeviceSerializer(s.ModelSerializer):
    class Meta:
        model = Device
        fields = ('name','created','uuid','screenshots','chavers','id','latest_screenshot','user')
        read_only_fields = ('created','uuid','screenshots','chavers','id','latest_screenshot','user')

class ScreenshotSerializer(s.ModelSerializer):
    class Meta:
        model = Screenshot
        fields = ('id', 'image', 'created')

class ChaverSerializer(s.ModelSerializer):
    class Meta:
        model = Chaver
        fields = ('id', 'name', 'email',"device", 'created')

class RegisterDeviceSerializer(s.Serializer):
    code = s.CharField(max_length=100)
    
