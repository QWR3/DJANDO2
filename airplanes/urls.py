from django.urls import path

from airplanes.views import AirplaneListCreateView, AirplaneReadUpdateDeleteView

urlpatterns = [
    path('', AirplaneListCreateView.as_view(), name='airplane_list_create'),
    path('<int:pk>/', AirplaneReadUpdateDeleteView.as_view(), name='airplane_read_update_delete'),
]