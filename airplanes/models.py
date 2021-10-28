from datetime import datetime
from django.db import models
from django.core import validators as v


# Create your models here.
class AirplaneModel(models.Model):
    class Meta():
        db_table = 'Airplanes'

    model = models.CharField(max_length=255, validators=[
        v.MinLengthValidator(3),
    ], unique=True)
    brand = models.CharField(max_length=255, validators=[
        v.MinLengthValidator(3),
    ])
    year = models.IntegerField(validators=[
        v.MinValueValidator(1950),
        v.MaxValueValidator(datetime.now().year)
    ])
    number_of_passengers = models.IntegerField()
    max_speed = models.IntegerField()
    max_distance = models.IntegerField()
