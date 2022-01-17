# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from cars.models import CarModel
from cars.serializers import CarSerializer


# class CarListCreateView(GenericAPIView):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all
#
#     def get(self, *args, **kwargs):
#         cars = self.queryset()
#         serializer = self.serializer_class(instance=cars, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = self.serializer_class(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class CarReadUpdateDelete(GenericAPIView):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get(self, *args, **kwargs):
#         car = self.get_object()
#         serializer = self.serializer_class(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         car = self.get_object()
#         data = self.request.data
#         serializer = self.serializer_class(car, data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         car = self.get_object()
#         data = self.request.data
#         serializer = self.serializer_class(car, data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         self.get_object().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer

    # queryset = CarModel.objects.all()

    def get_queryset(self):
        qs = CarModel.objects.all()
        # qs.filter(year__lte=2022)
        brand = self.request.query_params.get('brand')
        if brand:
            qs = qs.filter(brand__iexact=brand)
        qs = qs.order_by('-id')
        qs = [qs.last()]
        return qs


class CarReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
