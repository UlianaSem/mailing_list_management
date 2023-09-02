# from datetime import datetime, time
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from mailing_list.models import MailingListSettings
# from mailing_list.services import send_mail_now, send_delayed_message


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
    #
    # def dispatch(self, request, *args, **kwargs):
    #     response = super().dispatch(request)
    #
    #     if request.method == 'POST':
    #         start_time = request.POST.get('start_time')
    #         end_time = request.POST.get('end_time')
    #         # periodicity = request.POST.get('periodicity')
    #         # status = request.POST.get('status')
    #         users = request.POST.getlist('users')
    #         print(request.POST.get('pk'))
    #
    #         now = datetime.now().time()
    #
    #         if (datetime.strptime(start_time, '%H:%M:%S').time() < now <
    #                 datetime.strptime(end_time, '%H:%M:%S').time()):
    #             send_mail_now(users)
    #
    #         else:
    #             send_delayed_message(users)
    #
    #     return response


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
