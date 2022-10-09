from rest_framework.serializers import ModelSerializer

from .models import Device, Screenshot, Chaver

class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ('name',)
        read_only_fields = ('id', 'created','uuid','screenshots','chavers','id')

class ScreenshotSerializer(ModelSerializer):
    class Meta:
        model = Screenshot
        fields = ('id', 'image', 'created')

class ChaverSerializer(ModelSerializer):
    class Meta:
        model = Chaver
        fields = ('id', 'name', 'email', 'created')
