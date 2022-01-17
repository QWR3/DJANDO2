from django.urls import path

from cars.views import CarListCreateView, CarReadUpdateDelete

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car list create'),
    path('<int:pk>/', CarReadUpdateDelete.as_view(), name='car read update delete')
]
