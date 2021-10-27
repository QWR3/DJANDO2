from django.urls import path, include

from computers.views import ComputersListCreateView, ComputerReadUpdateDeleteView

urlpatterns = [
    path('', ComputersListCreateView.as_view(), name='computers_list_create'),
    path('<int:pk>/', ComputerReadUpdateDeleteView.as_view(), name='computer_read_update_delete'),
]
