# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0018_auto_20171117_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='interests',
            field=models.CharField(help_text='Enter your interests separated by commas', max_length=200, null=True),
        ),
    ]
