from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from django.template.loader import render_to_string
from .models import PostCategory, News
from .tasks import send_notification_email

@receiver(post_save, sender=User)
def add_user_to_common_group(sender, instance, created, **kwargs):
    if created:
        common_group, created = Group.objects.get_or_create(name='common')
        instance.groups.add(common_group)

@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers_emails = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        # Используем Celery для асинхронной отправки
        send_notification_email.delay(instance.preview(), instance.pk, instance.title, subscribers_emails)

@receiver(post_save, sender=News)
def post_save_news(sender, instance, created, **kwargs):
    if created:
        categories = instance.category.all()
        subscribers_emails = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        send_notification_email.delay(instance.preview(), instance.pk, instance.title, subscribers_emails)
