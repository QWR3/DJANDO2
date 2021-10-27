from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from computers.models import ComputerModel


class ComputersListCreateView(APIView):
    def get(self, *args, **kwargs):
        computers = ComputerModel.objects.all().values()
        return Response(computers, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data.dict()
        print(data)
        computer = ComputerModel.objects.create(**data)
        return Response(model_to_dict(computer), status.HTTP_201_CREATED)


class ComputerReadUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exclude = ComputerModel.objects.filter(id=pk).exclude()
        if not exclude:
            return Response(f'We have not any computer with id {pk}', status.HTTP_404_NOT_FOUND)
        computer = ComputerModel.objects.get(id=pk)
        print(computer)
        return Response(model_to_dict(computer), status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exclude = ComputerModel.objects.filter(id=pk).exclude()
        if not exclude:
            return Response(f'We have not any computer with id {pk}', status.HTTP_404_NOT_FOUND)
        data = self.request.data.dict()
        ComputerModel.objects.filter(id=pk).update(**data)
        computer = ComputerModel.objects.get(id=pk)
        return Response(model_to_dict(computer), status.HTTP_201_CREATED)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exclude = ComputerModel.objects.filter(id=pk).exclude()
        if not exclude:
            return Response(f'We have not any computer with id {pk}', status.HTTP_404_NOT_FOUND)
        ComputerModel.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
