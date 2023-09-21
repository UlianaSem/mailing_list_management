from django.urls import path
from mailing_list.views import (MailingListSettingsListView, MailingListSettingsCreateView,
                                MailingListSettingsUpdateView, MailingListSettingsDeleteView,
                                MailingListSettingsDetailView, LogListView, change_mailing_status)
from mailing_list.apps import MailingListConfig

app_name = MailingListConfig.name


urlpatterns = [
    path('', MailingListSettingsListView.as_view(), name='list'),
    path('create/', MailingListSettingsCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', MailingListSettingsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MailingListSettingsDeleteView.as_view(), name='delete'),
    path('view/<int:pk>/', MailingListSettingsDetailView.as_view(), name='view'),
    path('logs/', LogListView.as_view(), name='logs'),
    path('change_status/<int:pk>/', change_mailing_status, name='change_status'),
]
