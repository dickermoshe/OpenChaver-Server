from rest_framework.serializers import ModelSerializer

from .models import Device, Screenshot, Chaver

class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ('name','created','uuid','screenshots','chavers','id','latest_screenshot')
        read_only_fields = ('created','uuid','screenshots','chavers','id','latest_screenshot')

class ScreenshotSerializer(ModelSerializer):
    class Meta:
        model = Screenshot
        fields = ('id', 'image', 'created')

class ChaverSerializer(ModelSerializer):
    class Meta:
        model = Chaver
        fields = ('id', 'name', 'email',"device", 'created')
