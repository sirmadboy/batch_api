# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-05 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0021_auto_20170223_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='loadproc',
            name='ticket_code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ticket Code'),
        ),
    ]
