# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import FormView

from send_email import forms

USER_MODEL = get_user_model()


class EmailsViews(FormView):
    template_name = "choise_user.html"
    form_class = forms.FormEmail
    success_url = "/thanks/"

    def form_valid(self, form):
        form.send_email()
        return super(EmailsViews, self).form_valid(form)


def thanks(request):
    if request.method == "GET":
        return render(request, template_name="thanks.html")


def track_email(request, username):
    user = None
    try:
        user = USER_MODEL.objects.get(username=username)
    except ObjectDoesNotExist:
        user = False

    if user:
        user.subscriber.read_letter = True
        user.subscriber.save()

    return redirect("/")
