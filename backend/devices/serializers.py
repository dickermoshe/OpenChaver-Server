from rest_framework.serializers import ModelSerializer

from .models import Device, Screenshot, Chaver

class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ('name','created','uuid','screenshots','chavers','id')
        read_only_fields = ('created','uuid','screenshots','chavers','id')

class ScreenshotSerializer(ModelSerializer):
    class Meta:
        model = Screenshot
        fields = ('id', 'image', 'created')

class ChaverSerializer(ModelSerializer):
    class Meta:
        model = Chaver
        fields = ('id', 'name', 'email',"device", 'created')
