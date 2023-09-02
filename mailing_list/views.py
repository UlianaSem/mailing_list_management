from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from mailing_list.models import MailingListSettings


class MailingListSettingsListView(ListView):
    model = MailingListSettings
    extra_context = {
        'title': 'Список рассылок'
    }


class MailingListSettingsCreateView(CreateView):
    model = MailingListSettings
    fields = ['start_time', 'end_time', 'periodicity', 'status', 'users', ]
    success_url = reverse_lazy('mailing:list')
    extra_context = {
        'title': 'Создание рассылки'
    }


class MailingListSettingsUpdateView(UpdateView):
    model = MailingListSettings
    fields = ['start_time', 'end_time', 'periodicity', 'status', 'users', ]
    success_url = reverse_lazy('mailing:list')
    extra_context = {
        'title': 'Редактирование рассылки'
    }

    def get_success_url(self):
        return reverse('mailing:view', args=[self.object.pk])


class MailingListSettingsDeleteView(DeleteView):
    model = MailingListSettings
    success_url = reverse_lazy('mailing:list')
    extra_context = {
        'title': 'Удаление рассылки'
    }


class MailingListSettingsDetailView(DetailView):
    model = MailingListSettings
    extra_context = {
        'title': 'Подробная информация о рассылке'
    }
