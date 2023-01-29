import datetime

from celery import shared_task
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@shared_task
def send_message(context, email_layout, user_email, username):
    context["birthday"] = datetime.date.fromtimestamp(context["birthday"])
    context["image_url"] = "http://127.0.0.1:8000/send/track_email/{username}/".format(username=username)

    html_message = render_to_string(email_layout, context=context)
    plain_message = strip_tags(html_message)

    mail.send_mail(subject="{first} {last}".format(first=context["first_name"],
                                                   last=context["last_name"]),
                   message=plain_message,
                   from_email=settings.DEFAULT_FROM_EMAIL,
                   recipient_list=[user_email],
                   html_message=html_message, )

