from django.db import models
from django.core import validators as v


class PhoneModel(models.Model):
    class Meta:
        db_table = 'phones'

    diagonal = models.IntegerField(validators=[
        v.MinValueValidator(5),
        v.MaxValueValidator(8)
    ], blank=True, null=True)
    CPU = models.CharField(max_length=255, blank=True, default=0)
    RAM = models.IntegerField(validators=[
        v.MinValueValidator(2),
        v.MaxValueValidator(8)
    ], blank=True, default=0)
    camera = models.IntegerField(validators=[
        v.MinValueValidator(5),
        v.MaxValueValidator(128)
    ], blank=True, default=0)
    price = models.IntegerField(validators=[
        v.MinValueValidator(2700),
        v.MaxValueValidator(28000)
    ])
    model = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
