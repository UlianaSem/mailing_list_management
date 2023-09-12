from django.contrib import admin
from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['pk', 'email', 'name', ]
    list_filter = ['name', ]
    search_fields = ['email', 'name', 'comment', ]
