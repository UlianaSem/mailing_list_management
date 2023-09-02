from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(models.Model):
    email = models.EmailField(max_length=150, unique=True, verbose_name='email')
    name = models.CharField(max_length=250, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'клиент рассылки'
        verbose_name_plural = 'клиенты рассылки'
