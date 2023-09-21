from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterCreateView, pass_verification, block_user, UserListView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('verification/<int:pk>', pass_verification, name='verification'),
    path('list/', UserListView.as_view(), name='list'),
    path('block/<int:pk>/', block_user, name='block_user'),
]
