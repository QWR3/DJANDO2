from rest_framework import serializers as s

from cars.models import CarModel


class CarSerializer(s.ModelSerializer):
    class Meta:
        model = CarModel
        fields = "__all__"
    # ToDo валідації
