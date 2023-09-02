from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'email', 'name', ]
    list_filter = ['name', ]
    search_fields = ['email', 'name', 'comment', ]
