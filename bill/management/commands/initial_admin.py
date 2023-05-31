from django.core.management.base import BaseCommand

from django.contrib.auth.models import User

from bill_book.environments import Env


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Env.ADMIN_USER is None:
            return

        assert Env.ADMIN_PASS is not None

        if not User.objects.filter(username=Env.ADMIN_USER).exists():
            User.objects.create_superuser(
                username=Env.ADMIN_USER,
                password=Env.ADMIN_PASS
            )
