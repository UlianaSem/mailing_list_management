from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from user.models import User


class UserListView(ListView):
    model = User
    extra_context = {
        'title': 'Список пользователей'
    }


class UserCreateView(CreateView):
    model = User
    fields = ['email', 'name', 'comment', ]
    success_url = reverse_lazy('user:list')
    extra_context = {
        'title': 'Создание пользователя'
    }


class UserUpdateView(UpdateView):
    model = User
    fields = ['email', 'name', 'comment', ]
    success_url = reverse_lazy('user:list')
    extra_context = {
        'title': 'Редактирование пользователя'
    }

    def get_success_url(self):
        return reverse('user:view', args=[self.object.pk])


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user:list')
    extra_context = {
        'title': 'Удаление пользователя'
    }


class UserDetailView(DetailView):
    model = User
    extra_context = {
        'title': 'Подробная информация о пользователе'
    }
