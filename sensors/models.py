from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Sensor(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    temperature = models.FloatField()
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "sensors")

    def __str__(self) -> str:
        return self.id