# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 16:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['duration'], 'verbose_name_plural': 'Education'},
        ),
    ]
