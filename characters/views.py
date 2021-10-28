from django.forms import model_to_dict
from rest_framework import status
from rest_framework.views import APIView, Response
from characters.models import CharacterModel
from characters.serializers import CharacterSerializer


class CharacterListCreateView(APIView):
    def get(self, *args, **kwargs):
        characters = CharacterModel.objects.all()
        characters_json = CharacterSerializer(instance=characters, many=True).data
        return Response(characters_json, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CharacterSerializer(data=data)
        is_valid = serializer.is_valid()
        if not is_valid:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CharacterReadUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exclude = CharacterModel.objects.filter(id=pk).exclude()
        if not exclude:
            return Response(f'Error. We haven\'t any character with id {pk}', status.HTTP_404_NOT_FOUND)
        character = CharacterModel.objects.get(id=pk)
        character_json = CharacterSerializer(instance=character).data
        return Response(character_json, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exclude = CharacterModel.objects.filter(id=pk).exclude()
        if not exclude:
            Response(f'We haven\'t any character with id {pk}', status.HTTP_404_NOT_FOUND)
        data = self.request.data
        object = CharacterModel.objects.get(id=pk)
        character = CharacterSerializer(instance=object, data=data)
        is_valid = character.is_valid()
        if not is_valid:
            return Response(character.errors, status.HTTP_400_BAD_REQUEST)
        character.save()
        return Response(character.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exclude = CharacterModel.objects.filter(id=pk).exclude()
        if not exclude:
            return Response(f'Error. We haven\'t any character with id {pk}', status.HTTP_404_NOT_FOUND)
        CharacterModel.objects.get(id=pk).delete()
        return Response(status= status.HTTP_204_NO_CONTENT)