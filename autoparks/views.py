from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from autoparks.models import AutoparkModel
from autoparks.serializer import AutoparkSerializer


class AutoparkListCreateView(ListCreateAPIView):
    queryset = AutoparkModel.objects.all()
    serializer_class = AutoparkSerializer


class AutoparkReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = AutoparkModel.objects.all()
    serializer_class = AutoparkSerializer
