from rest_framework import serializers as s

from airplanes.models import AirplaneModel


class AirplaneSerializer(s.ModelSerializer):
    class Meta:
        model = AirplaneModel
        fields = "__all__"

    def validate(self, validate_data: dict):
        brand: str = validate_data.get('brand')
        year = validate_data.get('year')
        if year <= 1991 and brand.lower() == 'boeing':
            raise s.ValidationError('Error, Boeing until 1991 year don\'t support')
        elif year == 1991:
            raise s.ValidationError('Error, year 1991 don\'t support')
        return validate_data

    def validate_model(self, model):
        if model == '777':
            raise s.ValidationError('Error, model \'777\' don\'t support')
