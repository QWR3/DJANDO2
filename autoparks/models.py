from django.contrib.auth import get_user_model
from django.db import models

UserMpdel = get_user_model()


# Create your models here.
class AutoparkModel(models.Model):
    class Meta:
        db_table = 'autopark'

    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserMpdel, on_delete=models.CASCADE, verbose_name='autoparks')

    def __str__(self):
        return self.name
