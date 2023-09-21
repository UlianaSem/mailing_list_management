from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from blog.models import Blog
from mailing_list.forms import MailingListSettingsForm, MessageForm
from mailing_list.models import MailingListSettings, Log, Message
from mailing_list.services import MailingListCacheMixin


class GetObjectMixin:

    def get_object(self, queryset):
        self.object = super().get_object(queryset)

        if self.object.owner != self.request.user:
            raise Http404

        return self.object


class GetContextDataMixin:

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(MailingListSettings, Message, extra=1, form=MessageForm)

        if self.request.method == 'POST':
            formset = MessageFormset(self.request.POST, instance=self.object)
        else:
            formset = MessageFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data


class MailingListSettingsListView(LoginRequiredMixin, PermissionRequiredMixin, MailingListCacheMixin, ListView):
    model = MailingListSettings
    permission_required = 'mailing_list.view_mailinglistsettings'
    extra_context = {
        'title': 'Список рассылок'
    }

    def get_queryset(self):
        queryset = self.get_mailing_list_cache()

        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        blog = Blog.objects.order_by("?")[:3]
        context_data['blog'] = blog

        context_data['all'] = context_data['object_list'].count()
        context_data['active'] = context_data['object_list'].filter(status=MailingListSettings.STARTED).count()

        mailing_list = context_data['object_list'].prefetch_related('clients')
        clients = set()
        [[clients.add(client.email) for client in mailing.clients.all()] for mailing in mailing_list]
        context_data['clients_count'] = len(clients)

        return context_data


class MailingListSettingsCreateView(LoginRequiredMixin, PermissionRequiredMixin, GetContextDataMixin, CreateView):
    model = MailingListSettings
    permission_required = 'mailing_list.add_mailinglistsettings'
    form_class = MailingListSettingsForm
    success_url = reverse_lazy('mailing:list')
    extra_context = {
        'title': 'Создание рассылки'
    }

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

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


class MailingListSettingsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, GetObjectMixin, GetContextDataMixin,
                                    UpdateView):
    model = MailingListSettings
    permission_required = 'mailing_list.change_mailinglistsettings'
    form_class = MailingListSettingsForm
    extra_context = {
        'title': 'Редактирование рассылки'
    }

    def get_success_url(self):
        return reverse('mailing:view', args=[self.object.pk])

    def get_object(self, queryset=None):
        return super().get_object(queryset)

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class MailingListSettingsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, GetObjectMixin, DeleteView):
    model = MailingListSettings
    permission_required = 'mailing_list.delete_mailinglistsettings'
    success_url = reverse_lazy('mailing:list')
    extra_context = {
        'title': 'Удаление рассылки'
    }

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class MailingListSettingsDetailView(LoginRequiredMixin, PermissionRequiredMixin, GetObjectMixin, DetailView):
    model = MailingListSettings
    permission_required = 'mailing_list.view_mailinglistsettings'
    extra_context = {
        'title': 'Подробная информация о рассылке'
    }

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class LogListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Log
    permission_required = 'mailing_list.add_log'
    extra_context = {
        'title': 'Логи рассылок'
    }

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.is_staff:
            ids = MailingListSettings.objects.filter(owner=self.request.user).values_list('id')
            queryset = queryset.filter(mailing_list_id__in=ids)

        return queryset


@login_required
@permission_required('mailing_list.change_status')
def change_mailing_status(request, pk):
    fields = ('status')
    mailing_list_item = get_object_or_404(MailingListSettings, pk=pk)

    if (mailing_list_item.status == MailingListSettings.STARTED
            or mailing_list_item.status == MailingListSettings.CREATED):
        mailing_list_item.status = MailingListSettings.COMPLETED
    else:
        mailing_list_item.status = MailingListSettings.CREATED

    mailing_list_item.save()

    return redirect(reverse('mailing:list'))
