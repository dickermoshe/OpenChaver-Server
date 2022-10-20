from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from django.contrib.auth import get_user_model

from devices.serializers import DeviceSerializer

user_model = get_user_model()

class UserSerializer(BaseUserSerializer):
    devices = DeviceSerializer(many=True, read_only=True)
    class Meta(BaseUserSerializer.Meta):
        model = user_model
        fields = ('id', 'email', 'is_active','first_name','last_name','devices')

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = user_model
        fields = ('id', 'email', 'password','first_name','last_name')

