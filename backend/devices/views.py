from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions

from .models import Device, Screenshot, Chaver
from .serializers import DeviceSerializer, ScreenshotSerializer, ChaverSerializer

class DevicePermission(permissions.BasePermission):
    # Must be authenticated to access this view
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    # Must be the owner of the device to access it
    # The device must be in the user's devices list
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
        
class ScreenShotPermission(permissions.BasePermission):
    # Must be authenticated to access this view
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    # Must be the owner of the device to access it
    # The device must be in the user's devices list
    def has_object_permission(self, request, view, obj):
        return obj.device.user == request.user

class ChaverPermission(permissions.BasePermission):
    # Must be authenticated to access this view
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    # Must be the owner of the device to access it
    # The device must be in the user's devices list
    def has_object_permission(self, request, view, obj):
        return obj.device.user == request.user


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [DevicePermission]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(chaver=self.request.user)

# Allo all except delete and update
class ScreenshotViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
    ):

    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer
    permission_classes = [ScreenShotPermission]

    def get_queryset(self):
        return self.queryset.filter(device__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(device=self.request.user)

class ChaverViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):
    queryset = Chaver.objects.all()
    serializer_class = ChaverSerializer
    permission_classes = [ChaverPermission]

    def get_queryset(self):
        return self.queryset.filter(device__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(device=self.request.user)