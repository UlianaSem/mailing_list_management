from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from clients.models import Client


class ClientListView(ListView):
    model = Client
    extra_context = {
        'title': 'Список пользователей'
    }


class ClientCreateView(CreateView):
    model = Client
    fields = ['email', 'name', 'comment', ]
    success_url = reverse_lazy('clients:list')
    extra_context = {
        'title': 'Создание пользователя'
    }


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['email', 'name', 'comment', ]
    success_url = reverse_lazy('clients:list')
    extra_context = {
        'title': 'Редактирование пользователя'
    }

    def get_success_url(self):
        return reverse('clients:view', args=[self.object.pk])


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:list')
    extra_context = {
        'title': 'Удаление пользователя'
    }


class ClientDetailView(DetailView):
    model = Client
    extra_context = {
        'title': 'Подробная информация о пользователе'
    }
