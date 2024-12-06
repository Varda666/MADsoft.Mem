from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email="admin1@mail.ru",
            name="Admin",
        )

        user.set_password('123qwe')
        user.save()

