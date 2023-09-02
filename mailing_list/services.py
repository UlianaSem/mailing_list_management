from django.core.mail import send_mail
from django.conf import settings
import django.utils.timezone

from mailing_list.models import Message, MailingListSettings, Log


def _send_email(user, mailing):
    try:
        message = Message.objects.filter(status=Message.TO_BE_SENT)[0]

    except IndexError:
        pass

    result = send_mail(
        subject=message.subject,
        message=message.text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False
    )

    Log.objects.create(
        mailing_list=mailing.id,
        user=user.id,
        status=result,
        response=mailing,
    )


def send_mails():
    now = django.utils.timezone.datetime.now()

    for mailing in MailingListSettings.objects.filter(status=MailingListSettings.STARTED):

        if mailing.start_time < now < mailing.end_time:

            for mailing_client in mailing.objects.users.all():

                log = Log.objects.filter(
                    user=mailing_client,
                    mailing_list=mailing
                )

                if log.exists():
                    last_try_date = log.order_by('-time').first().time

                    if mailing.periodicity == MailingListSettings.DAILY:
                        if (now - last_try_date) >= MailingListSettings.DAILY:
                            _send_email(mailing_client, mailing)

                    elif mailing.periodicity == MailingListSettings.WEEKLY:
                        if (now - last_try_date) >= MailingListSettings.WEEKLY:
                            _send_email(mailing_client, mailing)

                    elif mailing.periodicity == MailingListSettings.MONTHLY:
                        if (now - last_try_date) >= MailingListSettings.MONTHLY:
                            _send_email(mailing_client, mailing)

                else:
                    _send_email(mailing_client, mailing)
