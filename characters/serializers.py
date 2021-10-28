from rest_framework import serializers as s

from characters.models import CharacterModel


class CharacterSerializer(s.ModelSerializer):
    class Meta:
        model = CharacterModel
        fields = '__all__'

    def validate_gender(self, gender: str):
        if gender.lower() == 'male' or gender.lower() == 'female':
            return gender
        raise s.ValidationError('Error. What are you?')

