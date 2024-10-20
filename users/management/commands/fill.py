from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        payment = [
            {
                "user": 1,
                "pay_date": "20.10.2024",
                "paid_course": True,
                "paid_lesson": True,
                "amount": 5000,
                "payment_method": "card",
            },
            {
                "user": 2,
                "pay_date": "21.10.2024",
                "paid_course": False,
                "paid_lesson": True,
                "amount": 7000,
                "payment_method": "card",
            },
            {
                "user": 3,
                "pay_date": "22.10.2024",
                "paid_course": True,
                "paid_lesson": False,
                "amount": 2000,
                "payment_method": "cash",
            }
        ]
