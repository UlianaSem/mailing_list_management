from django.urls import path
from clients.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView
from clients.apps import ClientConfig

app_name = ClientConfig.name


urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='delete'),
    path('view/<int:pk>/', ClientDetailView.as_view(), name='view'),
]