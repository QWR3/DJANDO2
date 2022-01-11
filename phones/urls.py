from django.urls import path

from phones.views import PhoneListCreateView, PhoneReadUpdateDeleteView

urlpatterns = [
    path('', PhoneListCreateView.as_view(), name="Phone list create"),
    path('<int:pk>/', PhoneReadUpdateDeleteView.as_view(), name="Phone read update delete")
]
