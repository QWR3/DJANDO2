from rest_framework import serializers as s

from autoparks.models import AutoparkModel
from cars.serializers import CarSerializer


class AutoparkSerializer(s.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoparkModel
        fields = ['id', 'name', 'city', 'cars']
