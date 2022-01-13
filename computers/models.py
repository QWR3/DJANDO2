from django.db import models
from django.core import validators as v


# Create your models here.
class ComputerModel(models.Model):
    class Meta:
        db_table = 'computers'

    CPU = models.CharField(max_length=255)
    memory = models.IntegerField(validators=[
        v.MinValueValidator(2),
        v.MaxValueValidator(8)
    ])
    storage = models.IntegerField(validators=[
        v.MinValueValidator(256),
        v.MaxValueValidator(1024)
    ])
    motherboard = models.CharField(max_length=255, null=True, blank=True)
