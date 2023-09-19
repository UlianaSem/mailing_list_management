from django.db import models

from mailing_list.models import NULLABLE


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое статьи')
    picture = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    view_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')
    publish_date = models.DateField(auto_now_add=True, verbose_name='дата публикации')

    def __str__(self):
        return f'{self.title} от {self.publish_date}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блог'
