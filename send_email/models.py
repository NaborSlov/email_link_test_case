# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models

USER_MODEL = get_user_model()


class EmailLayout(models.Model):
    title = models.CharField(max_length=50, verbose_name="name layout")
    path_layout = models.CharField(max_length=50, verbose_name="path to layout")

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    user = models.OneToOneField(USER_MODEL, on_delete=models.CASCADE)
    birthday = models.DateField()
    read_letter = models.BooleanField(default=False)


