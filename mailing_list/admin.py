from django.contrib import admin
from mailing_list.models import MailingListSettings, Message, Log


@admin.register(MailingListSettings)
class MailingListSettingsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'start_time', 'end_time', 'periodicity', 'status', ]
    list_filter = ['start_time', 'end_time', 'periodicity', 'status', ]
    search_fields = ['start_time', 'end_time', ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'mailing_list', 'subject', ]
    list_filter = ['mailing_list', ]
    search_fields = ['subject', 'text', ]


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['pk', 'mailing_list', 'time', 'status', ]
    list_filter = ['mailing_list', 'status', ]
    search_fields = ['mailing_list', 'time', 'status', ]
