from django.urls import path

from .views import SensorCreateAPIView, SensorUpdateAPIView, MeasurementCreateAPIView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/', SensorCreateAPIView.as_view(), name='create_sensor'),
    path('sensor/<pk>/', SensorUpdateAPIView.as_view(), name='update_sensor'),
    path('measurement/', MeasurementCreateAPIView.as_view(), name='add_measurement'),
]