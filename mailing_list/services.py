from django.core.mail import send_mail
from django.conf import settings
import django.utils.timezone

from user.models import User
from mailing_list.models import Message, MailingListSettings, Log


def _send_mail(users):
    user_email = [User.objects.get(pk=int(pk)).email for pk in users]
    message_subject = Message.objects.filter(status='К отправке')[0].subject
    message_text = Message.objects.filter(status='К отправке')[0].text  # IndexError, error with choice message

    send_mail(
            message_subject,
            message_text,
            settings.EMAIL_HOST_USER,
            user_email,
        )

#     add adding Logs


# Если создается рассылка со временем старта в будущем, то отправка должна стартовать автоматически по
# наступлению этого времени без дополнительных действий со стороны пользователя системы.
def send_mails():
    now = django.utils.timezone.datetime.now()

    for mailing in MailingListSettings.objects.filter(status='Запущена'):

        if mailing.start_time < now < mailing.end_time:

            for mailing_client in mailing.objects.users.all():

                log = Log.objects.filter(
                    client

                )




# По ходу отправки сообщений должна собираться статистика(см.описание сущности «сообщение» и «логи» выше) по
# каждому сообщению для последующего формирования отчетов.


# Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными
# данными, на какое - то время вообще не принимать запросы.Нужна корректная обработка подобных ошибок.Проблемы с
# внешним сервисом не должны влиять на стабильность работ разрабатываемого сервиса рассылок.
