import logging

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication


from drf_spectacular.utils import extend_schema

from .models import Device, Screenshot, Chaver
from .serializers import DeviceSerializer, ScreenshotSerializer, ChaverSerializer, VerifyUninstallCodeSerializer, UninstallCodeSerializer,ScreenshotUploadSerializer

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


class DeviceViewSet(mixins.DestroyModelMixin,mixins.UpdateModelMixin, mixins.ListModelMixin,
                    mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [DevicePermission]


    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.registered:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)


    @extend_schema(
        request=None,
        responses={
            200: None,
            400: None
        },
    )
    @action(detail=True,
            methods=['post'],
            permission_classes=[permissions.AllowAny])
    def register_device(self, request,pk):
        """Register a device to the user's devices list """
        device = Device.objects.get(id=pk)
        if device.registered:
            return Response(status=status.HTTP_400_BAD_REQUEST,data={'error':"Device already registered"})
        else:
            logger.info(f"Device {pk} registered to user {request.user}")
            device.registered = True
            device.save()
            return Response(status=status.HTTP_200_OK)
    
    @extend_schema(request=ScreenshotUploadSerializer)
    @action(detail=True,
            methods=['post'],
            permission_classes=[permissions.AllowAny])
    def add_screenshot(self, request, pk):
        """Add a screenshot to the device's screenshots list """
        device = Device.objects.get(id=pk)
        serializer = ScreenshotUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data, device)
        return Response(status=status.HTTP_200_OK)

# All all except delete
class ScreenshotViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):

    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer
    permission_classes = [ScreenShotPermission]

    def get_queryset(self):
        return self.queryset.filter(device__user=self.request.user)
    
    @extend_schema(request=None, responses={200: ScreenshotSerializer})
    @action(detail=True, methods=['post'])
    def false_positive(self, request, pk=None):
        """This endpoint is for a user or chaver to declare a screenshot as a false positive"""
        screenshot = Screenshot.objects.get(id=pk)
        screenshot.false_positive = True
        screenshot.save()
        return Response(ScreenshotSerializer(screenshot).data)



class ChaverViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Chaver.objects.all()
    serializer_class = ChaverSerializer
    permission_classes = [ChaverPermission]

    def get_queryset(self):
        return self.queryset.filter(device__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(device=self.request.data['device'])
    
    def destroy(self, request, *args, **kwargs):
        chaver:Chaver = self.get_object()
        chaver.send_uninstall_email()
        return super().destroy(request, *args, **kwargs)



@permission_classes([permissions.IsAdminUser])
@authentication_classes([TokenAuthentication])
@api_view(['POST'])
def send_reports(request):
    """Send reports to all users"""
    for user in Device.objects.all():
        user.send_report()
    return Response(status=status.HTTP_200_OK)
