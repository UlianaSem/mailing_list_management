from django.forms import inlineformset_factory
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from mailing_list.forms import MailingListSettingsForm, MessageForm
from mailing_list.models import MailingListSettings, Log, Message


class MailingListSettingsListView(ListView):
    model = MailingListSettings
    extra_context = {
        'title': 'Список рассылок'
    }

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)

        return queryset


class MailingListSettingsCreateView(CreateView):
    model = MailingListSettings
    form_class = MailingListSettingsForm
    success_url = reverse_lazy('mailing:list')
    extra_context = {
        'title': 'Создание рассылки'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(MailingListSettings, Message, extra=1, form=MessageForm)

        if self.request.method == 'POST':
            formset = MessageFormset(self.request.POST, instance=self.object)
        else:
            formset = MessageFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class MailingListSettingsUpdateView(UpdateView):
    model = MailingListSettings
    form_class = MailingListSettingsForm
    extra_context = {
        'title': 'Редактирование рассылки'
    }

    def get_success_url(self):
        return reverse('mailing:view', args=[self.object.pk])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        if self.object.owner != self.request.user:
            raise Http404

        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(MailingListSettings, Message, extra=1, form=MessageForm)

        if self.request.method == 'POST':
            formset = MessageFormset(self.request.POST, instance=self.object)
        else:
            formset = MessageFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class MailingListSettingsDeleteView(DeleteView):
    model = MailingListSettings
    success_url = reverse_lazy('mailing:list')
    extra_context = {
        'title': 'Удаление рассылки'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        if self.object.owner != self.request.user:
            raise Http404

        return self.object


class MailingListSettingsDetailView(DetailView):
    model = MailingListSettings
    extra_context = {
        'title': 'Подробная информация о рассылке'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        if self.object.owner != self.request.user:
            raise Http404

        return self.object


class LogListView(ListView):
    model = Log
    extra_context = {
        'title': 'Логи рассылок'
    }

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.is_staff:
            ids = MailingListSettings.objects.filter(owner=self.request.user).values_list('id')
            queryset = queryset.filter(mailing_list_id__in=ids)

        return queryset
