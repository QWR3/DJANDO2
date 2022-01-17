from datetime import datetime

from django.core import validators as v
from django.db import models

from autoparks.models import AutoparkModel


# Create your models here.


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField(validators=[
        v.MinValueValidator(1980),
        v.MaxValueValidator(datetime.now().year)
    ])
    autopark = models.ForeignKey(AutoparkModel, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.model + ' ' + self.brand
