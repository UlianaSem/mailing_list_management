from django.core.management import BaseCommand
from mailing_list.services import send_mails


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_mails()
