from rest_framework.serializers import ModelSerializer

from .models import Device, Screenshot, Chaver

class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'name', 'created','screenshots','chavers')
        read_only_fields = ('id', 'created','uuid')

class ScreenshotSerializer(ModelSerializer):
    class Meta:
        model = Screenshot
        fields = ('id', 'image', 'created')

class ChaverSerializer(ModelSerializer):
    class Meta:
        model = Chaver
        fields = ('id', 'name', 'email', 'created')
