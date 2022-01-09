from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from computers.models import ComputersModel


class ComputerListCreateView(APIView):
    def get(self, *args, **kwargs):
        computers = ComputersModel.objects.all().values()
        return Response(computers, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data.dict()
        computer = ComputersModel.objects.create(**data)
        return Response(status=status.HTTP_201_CREATED)


class ComputerReadUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = ComputersModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        computer = ComputersModel.objects.get(pk=pk)
        return Response(model_to_dict(computer), status.HTTP_200_OK)
    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = ComputersModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = self.request.data.dict()
        ComputersModel.objects.filter(pk=pk).update(**data)
        return Response(status=status.HTTP_200_OK)
    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = ComputersModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ComputersModel.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
