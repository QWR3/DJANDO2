from django.urls import path

from computers.views import ComputerListCreateView, ComputerReadUpdateDeleteView

urlpatterns = [
    path('', ComputerListCreateView.as_view(), name="Computer list create"),
    path('<int:pk>/', ComputerReadUpdateDeleteView.as_view(), name="computer read update delete")
]
