# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0016_auto_20171117_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(choices=[('bt', 'Bachelor of Technology (B.Tech)'), ('bs', 'Bachelor of Science (B.Sc)'), ('be', 'Bachelor of Engineering (B.E.)'), ('mt', 'Master of Technology (M.Tech)'), ('ms', 'Master of Science (M.Sc)'), ('ph', 'Doctor of Philosophy (Ph.D.')], help_text='Degree obtained', max_length=2),
        ),
    ]
