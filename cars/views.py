from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from cars.models import CarModel


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all().values()
        return Response(cars)

    def post(self, *args, **kwargs):
        data = self.request.data.dict()
        car = CarModel.objects.create(**data)
        return Response(model_to_dict(car))


class CarReadUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response("Go go away")
        car = CarModel.objects.get(pk=pk)
        return Response(model_to_dict(car))

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response("yps")
        data = self.request.data.dict()
        CarModel.objects.filter(pk=pk).update(**data)
        car = CarModel.objects.get(pk=pk)
        print(car)
        return Response(model_to_dict(car))

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('go go away')
        CarModel.objects.filter(pk=pk).delete()
        return Response('')
