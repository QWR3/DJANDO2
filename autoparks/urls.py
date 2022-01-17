from django.urls import path

from autoparks.views import AutoparkReadUpdateDeleteView, AutoparkListCreateView

urlpatterns = [
    path('', AutoparkListCreateView.as_view(), name='autopark list create'),
    path('<int:pk>/', AutoparkReadUpdateDeleteView.as_view(), name='autopark read update delete')
]
