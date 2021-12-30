from django.urls import path

from cars.views import CarListCreateView, CarReadUpdateDeleteView

urlpatterns = [
    path('', CarListCreateView.as_view(), name="car_list_create"),
    path('<int:pk>/', CarReadUpdateDeleteView.as_view(), name="car_read_update_delete"),

]
