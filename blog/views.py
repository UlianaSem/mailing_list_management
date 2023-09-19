from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Наш блог'
    }


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {
        'title': 'Наш блог'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()

        return self.object
