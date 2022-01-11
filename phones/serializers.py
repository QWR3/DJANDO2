from rest_framework import serializers as s

from phones.models import PhoneModel


class PhoneSerializer(s.ModelSerializer):
    class Meta:
        model = PhoneModel
        fields = '__all__'

    def validate(self, validated_data:dict):
        return validated_data

