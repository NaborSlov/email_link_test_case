# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-01-29 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_email', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='read_letter',
            field=models.BooleanField(default=False),
        ),
    ]
