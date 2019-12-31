from django.db import models

# Create your models here.

class Location(models.Model):
    longitude = models.DecimalField(max_digits=999, decimal_places=3)
    latitude = models.DecimalField(max_digits=999, decimal_places=3)