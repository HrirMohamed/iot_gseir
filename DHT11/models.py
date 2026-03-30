from django.db import models

class DHT11(models.Model):

    temperature = models.FloatField()
    humidite = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"T={self.temperature} H={self.humidite}"
from django.db import models

# Create your models here.
