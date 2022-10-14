import logging
from urllib import request

from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import action, api_view

from drf_spectacular.utils import extend_schema

from .models import Device, Screenshot, Chaver
from .serializers import DeviceSerializer, ScreenshotSerializer, ChaverSerializer, RegisterDeviceSerializer, VerifyUninstallCodeSerializer, UninstallCodeSerializer,ScreenshotUploadSerializer

logger = logging.getLogger(__name__)


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
        # Check if the user is trying to add a new chaver
        if request.method == 'POST':
            device = Device.objects.get(id=request.data['device'])
            return device.user == request.user
        else:
            return request.user.is_authenticated

    # Must be the owner of the device to access it
    # The device must be in the user's devices list
    def has_object_permission(self, request, view, obj):
        return obj.device.user == request.user


class DeviceViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
                    mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [DevicePermission]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(request=None, responses={200: UninstallCodeSerializer})
    @action(detail=True,
            methods=['get'],
            permission_classes=[DevicePermission])
    def uninstall_code(self, request, pk):
        """
        Get the uninstall code for the device
        The only way to remove a device from the user's devices list is to use the uninstall code
        """

        logger.info(
            f"Getting uninstall code for device {pk} from user {request.user}")

        device = self.get_object()

        for chaver in device.chavers.all():
            chaver: Chaver
            logger.info(
                f"Sending uninstall email to {chaver.name} from device {device.name}"
            )
            chaver.send_uninstall_email()

        return Response(UninstallCodeSerializer(device).data,
                        status=status.HTTP_200_OK)

    @extend_schema(request=VerifyUninstallCodeSerializer,
                   responses={
                       200: None,
                       400: None,
                   })
    @action(detail=False,
            methods=['post'],
            permission_classes=[permissions.AllowAny])
    def verify_uninstall_code(self, request):
        """Verify the uninstall code for the device"""
        serializer = VerifyUninstallCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:    
            device = Device.objects.get(
            device_id=serializer.validated_data['device_id'])
        except Device.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if device.verify_uninstall_code(
                serializer.validated_data['uninstall_code']):
            for chaver in device.chavers.all():
                chaver: Chaver
                logger.info(
                    f"Sending uninstall email to {chaver.name} from device {device.name}"
                )
                chaver.send_uninstall_email()
            device.delete()
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=RegisterDeviceSerializer,
        responses={
            200: DeviceSerializer,
            400: None
        },
    )
    @action(detail=False,
            methods=['post'],
            permission_classes=[permissions.AllowAny])
    def register_device(self, request):
        """Register a device to the user's devices list """
        serializer = RegisterDeviceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            device = Device.objects.get(
                device_id=serializer.validated_data['device_id'])
            if not device.registered:
                device.registered = True
                device.save()
                return Response(DeviceSerializer(device).data,
                                status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Device.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# All all except delete
class ScreenshotViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):

    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer
    permission_classes = [ScreenShotPermission]

    def get_queryset(self):
        return self.queryset.filter(device__user=self.request.user)

    @action(detail=True, methods=['post'])
    def false_positive(self, request, pk=None):
        """This endpoint is for a user or chaver to declare a screenshot as a false positive"""
        screenshot = Screenshot.objects.get(id=pk)
        screenshot.false_positive = True
        screenshot.save()
        return Response(status=status.HTTP_200_OK)

    @extend_schema(request=ScreenshotUploadSerializer)
    @action(detail=False,
            methods=['post'],
            permission_classes=[permissions.AllowAny])
    def add_screenshot(self, request):
        """Add a screenshot to the device's screenshots list """
        s = ScreenshotUploadSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        screenshot = s.create(s.validated_data)
        return Response(ScreenshotSerializer(screenshot).data,)


class ChaverViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Chaver.objects.all()
    serializer_class = ChaverSerializer
    permission_classes = [ChaverPermission]

    def get_queryset(self):
        return self.queryset.filter(device__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(device=self.request.data['device'])
    
    @extend_schema(request=None, responses={200: None})
    @action(detail=True, methods=['post'])
    def remove_chaver(self, request, pk):
        """This function removes a chaver from a device"""
        chaver:Chaver = self.get_object()
        chaver.send_uninstall_email()
        chaver.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def send_reports(request):
    """Send reports to all users"""
    for user in Device.objects.all():
        user.send_report()
    return Response(status=status.HTTP_200_OK)
