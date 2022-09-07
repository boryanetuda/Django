from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from .views import SensorViewSet, MeasurementViewSet

router = DefaultRouter()
router.register('sensors', SensorViewSet)
router.register('Measurement', MeasurementViewSet)

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]