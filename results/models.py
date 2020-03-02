from django.db import models

# Create your models here.
class Restauraunt(models.Model):
    name = models.CharField(max_length=30)
    rating = models.DecimalField(max_digits=10, decimal_places=3)
    phone_num = models.CharField(max_length=10)
    price = models.CharField(max_length=10)

    # string representation of model
    def __str__(self):
        return self.title