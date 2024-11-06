from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from materials.models import Subscription


@shared_task
def mail_update_course_info(course_id):
    """Функция отправки сообщения об обновлении курса"""
    course_subscriptions = Subscription.objects.filter(course=course_id)
    for subscription in course_subscriptions:
        send_mail(
            subject="Обновление материалов курса",
            message=f'Курс {subscription.course.title} был обновлен.',
            from_email=EMAIL_HOST_USER,
            recipient_list=[subscription.user.email],
            fail_silently=False
        )
