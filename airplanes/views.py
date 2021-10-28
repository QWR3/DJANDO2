from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from airplanes.models import AirplaneModel
from airplanes.serializer import AirplaneSerializer


class AirplaneListCreateView(APIView):
    def get(self, *args, **kwargs):
        airplanes = AirplaneModel.objects.all()
        serializer = AirplaneSerializer(instance=airplanes, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data.dict()
        serializer = AirplaneSerializer(data=data)
        is_valid = serializer.is_valid()
        if not is_valid:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class AirplaneReadUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exclude = AirplaneModel.objects.filter(id=pk).exclude()
        if not exclude:
            return Response(f'Sorry, but we have not any airplane with id {pk}', status.HTTP_404_NOT_FOUND)
        airplane = AirplaneSerializer(AirplaneModel.objects.get(id=pk))
        return Response(airplane.data)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exclude = AirplaneModel.objects.filter(id=pk).exclude()
        if not exclude:
            return Response(f'Sorry, but we have not any airplane with id {pk}', status.HTTP_404_NOT_FOUND)
        data = self.request.data
        airplane = AirplaneModel.objects.get(id=pk)
        serializer = AirplaneSerializer(instance=airplane, data=data)
        is_valid = serializer.is_valid()
        if not is_valid:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        if not AirplaneModel.objects.filter(pk=pk).exclude():
            return Response(f'Sorry, but we have not any airplane with id {pk}', status.HTTP_404_NOT_FOUND)
        AirplaneModel.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

