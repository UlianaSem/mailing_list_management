from datetime import timedelta, time

from django.db import models
from user.models import User


NULLABLE = {'blank': True, 'null': True}


class MailingListSettings(models.Model):
    DAILY = timedelta(days=1)
    WEEKLY = timedelta(days=7)
    MONTHLY = timedelta(days=30, hours=12)

    PERIODICITY_CHOICES = [
        (DAILY, "Раз в день"),
        (WEEKLY, "Раз в неделю"),
        (MONTHLY, "Раз в месяц"),
    ]

    CREATED = 'Создана'
    STARTED = 'Запущена'
    COMPLETED = 'Завершена'

    STATUS_CHOICES = [
        (COMPLETED, "Завершена"),
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
    ]

    start_time = models.TimeField(verbose_name='время начала рассылки', default=time(hour=14))
    end_time = models.TimeField(verbose_name='время окончания рассылки', default=time(hour=15))
    periodicity = models.DurationField(verbose_name='периодичность', default=MONTHLY, choices=PERIODICITY_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=CREATED, verbose_name='статус рассылки')

    users = models.ManyToManyField(User, verbose_name='клиенты рассылки')

    def __str__(self):
        return f'time: {self.start_time} - {self.end_time}, periodicity: {self.periodicity}, status: {self.status}'

    class Meta:
        verbose_name = 'настройки рассылки'
        verbose_name_plural = 'настройки рассылки'


class Message(models.Model):
    TO_BE_SENT = 'К отправке'
    SHIPPED = 'Отправлено'

    STATUS_CHOICES = [
        (TO_BE_SENT, "К отправке"),
        (SHIPPED, "Отправлено"),
    ]

    mailing_list = models.ForeignKey(MailingListSettings, on_delete=models.CASCADE, verbose_name='рассылка')

    subject = models.CharField(max_length=250, verbose_name='тема письма')
    text = models.TextField(verbose_name='тело письма')

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=TO_BE_SENT, verbose_name='статус отправки')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Log(models.Model):
    mailing_list = models.ForeignKey(MailingListSettings, on_delete=models.DO_NOTHING, verbose_name='рассылка')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='клиент рассылки', **NULLABLE)

    time = models.DateTimeField(verbose_name='дата и время последней попытки')
    status = models.BooleanField(verbose_name='статус попытки')
    response = models.CharField(max_length=200, verbose_name='ответ почтового сервера', **NULLABLE)

    def __str__(self):
        return f'{self.time} {self.status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
