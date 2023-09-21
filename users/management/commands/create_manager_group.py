from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from mailing_list.models import MailingListSettings
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        group = Group.objects.create(
            name='Manager'
        )

        content_types = ContentType.objects.get_for_models(MailingListSettings, User).values()
        permission_list = Permission.objects.filter(codename__in=['view_mailinglistsettings', 'view_user',
                                                                  'change_status', 'set_active'],
                                                    content_type__in=content_types, )

        group.permissions.set(permission_list)
        group.save()
