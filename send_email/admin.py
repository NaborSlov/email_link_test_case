# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from send_email import models

admin.site.register(models.EmailLayout)
admin.site.register(models.Subscriber)
