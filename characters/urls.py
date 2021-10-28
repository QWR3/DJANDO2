from django.urls import path

from characters.views import CharacterListCreateView, CharacterReadUpdateDeleteView

urlpatterns = [
    path('', CharacterListCreateView.as_view(), name='characters_list_create'),
    path('<int:pk>/', CharacterReadUpdateDeleteView.as_view(), name='character_read_update_delete'),
]
