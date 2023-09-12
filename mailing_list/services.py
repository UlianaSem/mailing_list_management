from django.core.mail import send_mail
from django.conf import settings
import django.utils.timezone

from mailing_list.models import Message, MailingListSettings, Log


def _send_email(client, mailing, message):
    result = send_mail(
        subject=message.subject,
        message=message.text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[client.email],
        fail_silently=False,
    )
    print(result)
    Log.objects.create(
        mailing_list=mailing,
        client=client,
        status=result,
    )


def send_mails():
    now = django.utils.timezone.datetime.now()
    now_time = now.time()

    for mailing in MailingListSettings.objects.filter(status=MailingListSettings.STARTED):
        print(mailing)

        if mailing.start_time < now_time < mailing.end_time:

            for mailing_client in mailing.clients.all():

                message = mailing.message_set.filter(status=Message.TO_BE_SENT).first()
                print(message)

                if message is None:
                    return

                log = Log.objects.filter(
                    client=mailing_client,
                    mailing_list=mailing
                )

                if log.exists():

                    last_try_date = log.order_by('-time').first().time.replace(tzinfo=None)

                    if mailing.periodicity == MailingListSettings.DAILY:
                        if (now - last_try_date) >= MailingListSettings.DAILY:
                            _send_email(mailing_client, mailing, message)

                    elif mailing.periodicity == MailingListSettings.WEEKLY:
                        if (now - last_try_date) >= MailingListSettings.WEEKLY:
                            _send_email(mailing_client, mailing, message)

                    elif mailing.periodicity == MailingListSettings.MONTHLY:
                        if (now - last_try_date) >= MailingListSettings.MONTHLY:
                            _send_email(mailing_client, mailing, message)

                else:
                    _send_email(mailing_client, mailing, message)

            message.status = Message.SHIPPED
            message.save()
