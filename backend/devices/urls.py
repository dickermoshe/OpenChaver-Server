from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import DeviceViewSet ,ScreenshotViewSet, ChaverViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet, basename='devices')
router.register(r'screenshots', ScreenshotViewSet, basename='screenshots')
router.register(r'chavers', ChaverViewSet, basename='chavers')
