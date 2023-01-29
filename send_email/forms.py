# coding=utf-8
import calendar
import datetime
import json

from django import forms
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule

from send_email import models

USER_MODEL = get_user_model()


class MyModelChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.username


class FormEmail(forms.Form):
    users = MyModelChoiceField(label="Пользователи", queryset=USER_MODEL.objects.all(), )
    email_layout = forms.ModelChoiceField(label="Email шаблоны", queryset=models.EmailLayout.objects.all(), )

    def send_email(self):
        users = self.cleaned_data["users"]
        email_layout = self.cleaned_data["email_layout"].path_layout

        for user in users:
            birthday = user.subscriber.birthday
            birthday_context = calendar.timegm(birthday.timetuple())

            schedule, _ = CrontabSchedule.objects.get_or_create(
                minute="*",
                hour=12,
                day_of_week="*",
                day_of_month=birthday.day,
                month_of_year=birthday.month,
            )

            context = {"first_name": user.first_name,
                       "last_name": user.last_name,
                       "birthday": birthday_context}

            task, _ = PeriodicTask.objects.get_or_create(
                name="Birthday {username} {birthday}".format(username=user.username,
                                                             birthday=birthday),
                crontab=schedule,
                task="send_email.tasks.send_message",
                kwargs=json.dumps({
                    "context": context,
                    "email_layout": email_layout,
                    "user_email": user.email,
                    "username": user.username
                }),
            )
