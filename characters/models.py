from django.db import models
from django.core import validators as v


# Create your models here.
class CharacterModel(models.Model):
    class Meta:
        db_table = 'characters'

    name = models.CharField(validators=[v.MinLengthValidator(3)], max_length=255)
    status = models.CharField(blank=True, default='unknown', max_length=255)
    species = models.CharField(max_length=255)
    type = models.CharField(blank=True, max_length=255)
    gender = models.CharField(max_length=6)
