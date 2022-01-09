from django.urls import path

from computers.views import ComputerListCreateView, ComputerReadUpdateDeleteView

urlpatterns = [
    path('', ComputerListCreateView.as_view(), name='Computer list crate'),
    path('<int:pk>/', ComputerReadUpdateDeleteView.as_view(), name='Computer list crate')
]
