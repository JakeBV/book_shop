from django.core.mail import send_mail

from users.models import CustomUser


def send_email_admins():
    """Функция отправки email всем администраторам с доступным полем email"""
    superusers_emails = CustomUser.objects.filter(is_superuser=True).values_list('email')
    send_mail('This is test message', 'Любое содержание',
              'from@example.com', superusers_emails, fail_silently=False)
