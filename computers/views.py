from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from computers.models import ComputerModel
from computers.serializers import ComputerSerializer


class ComputerListCreateView(APIView):
    def get(self, *args, **kwargs):
        computers = ComputerModel.objects.all().values()
        return Response(computers, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = ComputerSerializer(data=data)
        is_valid = serializer.is_valid()
        if not is_valid:
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class ComputerReadUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = ComputerModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        computer = ComputerModel.objects.get(pk=pk)
        serializer = ComputerSerializer(computer)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = ComputerModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = self.request.data
        computer = ComputerModel.objects.get(pk=pk)
        serializer = ComputerSerializer(computer, data)
        is_valid = serializer.is_valid()
        if not is_valid:
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = ComputerModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ComputerModel.objects.filter(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
