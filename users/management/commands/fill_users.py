from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        users_list = [
            {   "id": 1,
                "email": "test1@mail.ru",
                "phone_number": "8977-777-7777",
                "city": "Moscow",
                "avatar": "",
            },
            {   "id": 2,
                "email": "test2@mail.ru",
                "phone_number": "8988-777-7777",
                "city": "SPB",
                "avatar": "",
            },
            {   "id": 3,
                "email": "test3@mail.ru",
                "phone_number": "8999-777-7777",
                "city": "Tver",
                "avatar": "",
            },
        ]
        users_creation = []
        for user in users_list:
            users_creation.append(User(**user))
        User.objects.bulk_create(users_creation)
