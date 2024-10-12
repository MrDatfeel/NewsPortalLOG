from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Post, Category
import datetime




@shared_task
def send_email_task(pk):
    post = Post.objects.get(pk=pk)
    categories = post.post.category.all()
    title = post.post_title
    subscribers_emails = []
    for category in categories:
        subscribers_user = category.subscribers.all()
        for sub_user in subscribers_user:
            subscribers_emails.append(sub_user.email)
    html_content = render_to_string(
        'subscribe.html',
        {
            'text' : f'{post.post_title}',
            'link' : f'{settings.SITE_URL}/news/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@shared_task
def weekly_send_email_task():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(date_creation__gte=last_week)
    categories = set(posts.values_list('post_category__category_name', flat=True))
    subscriberes = set(
        Category.objects.filter(category_name__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'weekly_newsletter.html',
        {
                'link': settings.SITE_URL,
                'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Your Weekly News Update',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()



