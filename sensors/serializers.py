# Rest framework
from rest_framework import serializers

# Customize
from sensors.models import Sensor

class SensorSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Sensor 
        fields = [ "id","x","y","z","temperature" ]
        read_only_fields = ["id","x","y","z"]