from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import DeviceViewSet ,ScreenshotViewSet, ChaverViewSet, LogViewSet,send_reports

router = DefaultRouter()
router.register(r'devices', DeviceViewSet, basename='devices')
router.register(r'screenshots', ScreenshotViewSet, basename='screenshots')
router.register(r'chavers', ChaverViewSet, basename='chavers')
router.register(r'logs', LogViewSet, basename='logs')


urlpatterns = [
    path('', include(router.urls)),
    path('send_reports/', send_reports, name='send_reports'),
]

