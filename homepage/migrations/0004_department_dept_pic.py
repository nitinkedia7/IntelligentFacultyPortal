# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20171114_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='dept_pic',
            field=models.ImageField(blank=True, help_text='Department Picture', null=True, upload_to='dept_pic'),
        ),
    ]