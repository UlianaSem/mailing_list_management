from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'view_count', 'publish_date', )
    list_filter = ('view_count', 'publish_date', )
    search_fields = ('title', 'content', 'publish_date', )
