from django.urls import path
from user.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, UserDetailView
from user.apps import UserConfig

app_name = UserConfig.name


urlpatterns = [
    path('', UserListView.as_view(), name='list'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', UserUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete'),
    path('view/<int:pk>/', UserDetailView.as_view(), name='view'),
]