from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
from phones.models import PhoneModel
from phones.serializers import PhoneSerializer


class PhoneListCreateView(APIView):
    def get(self, *args, **kwargs):
        phones = PhoneModel.objects.all()
        serializer = PhoneSerializer(instance=phones, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = PhoneSerializer(data=data)
        is_valid = serializer.is_valid()
        if not is_valid:
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)


class PhoneReadUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = PhoneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        phone = PhoneModel.objects.get(pk=pk)
        return Response(PhoneSerializer(instance=phone).data)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = PhoneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = self.request.data
        phone = PhoneModel.objects.get(pk=pk)
        serializer = PhoneSerializer(instance=phone, data=data)
        is_valid = serializer.is_valid()
        if not is_valid:
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = PhoneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        PhoneModel.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
