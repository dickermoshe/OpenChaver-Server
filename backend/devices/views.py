from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import Device, Screenshot, Chaver
from .serializers import DeviceSerializer, ScreenshotSerializer, ChaverSerializer , RegisterDeviceSerializer,VerifyUninstallCodeSerializer


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


class DeviceViewSet(mixins.UpdateModelMixin,
    mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [DevicePermission]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def remove_device(self, request, pk):
        """Remove a device from the user's devices list """
        device = Device.objects.get(id=pk)
        for chaver in device.chavers.all():
            send_mail(
                f'{device.user.email} removed you as a chaver.',
                'This email is to inform you that you have been removed as a chaver from the device: '
                + str(device.name),
                settings.EMAIL_HOST_USER,
                [chaver.email],
                fail_silently=False,
            )
            chaver.delete()
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def get_uninstall_code(self, request, pk):
        """Get the uninstall code for the device"""
        device = Device.objects.get(id=pk)
        return Response(device.get_uninstall_code(), status=status.HTTP_200_OK)
    
    @extend_schema(
        request=VerifyUninstallCodeSerializer,
        responses={
            200: None,
            400: None,
        }
    )
    @action(detail=False, methods=['post'])
    def verify_uninstall_code(self, request):
        """Verify the uninstall code for the device"""
        serializer = VerifyUninstallCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        device = Device.objects.get(uuid=serializer.validated_data['device_id'])
        if device.verify_uninstall_code(serializer.validated_data['uninstall_code']):
            device.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=RegisterDeviceSerializer,
        responses={200: DeviceSerializer, 400: None},
    )
    @action(detail=False,methods=['post'],permission_classes=[permissions.AllowAny])
    def register_device(self, request):
        """Register a device to the user's devices list """
        serializer = RegisterDeviceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:    
            device = Device.objects.get(uuid=serializer.validated_data['device_id'])
            if not device.registered:
                device.registered = True
                device.save()
                return Response(DeviceSerializer(device).data, status=status.HTTP_200_OK)
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
        screenshot = Screenshot.objects.get(id=pk)
        screenshot.false_positive = True
        screenshot.save()
        return Response(status=status.HTTP_200_OK)
    

    @action(detail=True, methods=['post'],permission_classes=[permissions.AllowAny])
    def add_screenshot(self, request, uuid):
        """Add a screenshot to the device's screenshots list """
        device = Device.objects.get(uuid=uuid)
        screenshot = Screenshot.objects.create(device=device, image=request.data['image'])
        return Response(status=status.HTTP_200_OK)

class ChaverViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Chaver.objects.all()
    serializer_class = ChaverSerializer
    permission_classes = [ChaverPermission]

    def get_queryset(self):
        return self.queryset.filter(device__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(device=self.request.data['device'])

    def remove_chaver(self, request, pk=None):
        """This function removes a chaver from a device"""
        chaver = Chaver.objects.get(id=pk)
        # Send email to chaver
        send_mail(
            f'{chaver.device.user.email} removed you as a chaver.',
            'This email is to inform you that you have been removed as a chaver from the device: '
            + str(chaver.device.name),
            settings.EMAIL_HOST_USER,
            [chaver.email],
            fail_silently=False,
        )
        chaver.delete()
        return Response(status=status.HTTP_200_OK)
