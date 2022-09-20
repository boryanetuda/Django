from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


class Measurement(models.Model):
    value = models.FloatField()
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, upload_to='media')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')