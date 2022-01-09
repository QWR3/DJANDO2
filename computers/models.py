from django.db import models


# Create your models here.
class ComputersModel(models.Model):
    class Meta:
        db_table = 'computers'

    RAM = models.IntegerField()
    processor = models.CharField(max_length=255)
    diagonal = models.IntegerField()
