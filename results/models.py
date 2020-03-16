from django.db import models
from roulette.models import Location

# Create your models here.
class Restauraunt(models.Model):
    foreign = models.ForeignKey(Location, null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    rating = models.DecimalField(max_digits=10, decimal_places=3)
    phone_num = models.CharField(max_length=20)
    price = models.CharField(max_length=20)

    # string representation of model
    def __str__(self):
        return self.name