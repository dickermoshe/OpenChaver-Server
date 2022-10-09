from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

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


class DeviceViewSet(mixins.UpdateModelMixin,
    mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [DevicePermission]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(chaver=self.request.user)

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


# Allo all except delete
class ScreenshotViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer
    permission_classes = [ScreenShotPermission]

    def get_queryset(self):
        return self.queryset.filter(device__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(device=self.request.user)

    @action(detail=True, methods=['post'])
    def false_positive(self, request, pk=None):
        screenshot = Screenshot.objects.get(id=pk)
        screenshot.false_positive = True
        screenshot.save()
        return Response(status=status.HTTP_200_OK)


class ChaverViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Chaver.objects.all()
    serializer_class = ChaverSerializer
    permission_classes = [ChaverPermission]

    def get_queryset(self):
        return self.queryset.filter(device__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(device=self.request.user)

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
