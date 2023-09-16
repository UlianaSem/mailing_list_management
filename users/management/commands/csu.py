import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.ru',
            first_name='Admin',
            last_name='Admin',
            code='0000',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )

        user.set_password(os.getenv('ADMIN_PASSWORD'))
        user.save()
