# Python
import random

# Rest framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Customize
from sensors.serializers import SensorSerialzier
from sensors.models import Sensor

class SensorViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SensorSerialzier

    def get_queryset(self):
        return Sensor.objects.filter(owner = self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def list(self, request, *args, **kwargs):
        sensors = Sensor.objects.filter(owner = self.request.user)
        for sensor in sensors:
            random_number = random.randrange(8,12,1)
            random_float = random.randrange(1,9,1)
            temperature = random_number + random_float/10
            data = {
                "temperature": temperature
            }
            sensor_serializer = SensorSerialzier(instance=sensor, data=data)
            sensor_serializer.is_valid(raise_exception=True)
            sensor_serializer.save()
        return super().list(request, *args, **kwargs)
