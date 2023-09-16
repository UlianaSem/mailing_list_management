from random import randint

from django.conf import settings
from django.core.mail import send_mail

from users.models import User


def _create_verification_code():
    code = ''.join([str(randint(0, 9)) for _ in range(4)])
    return code


def send_code(user_pk):
    user = User.objects.get(pk=user_pk)

    send_mail(
        subject='Вы зарегистрировали на сайте управления рассылками',
        message=f'Добро пожаловать на наш сайт! Пожалуйста, подтвердите вашу почту. Проверочный код: {user.code}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False
    )
