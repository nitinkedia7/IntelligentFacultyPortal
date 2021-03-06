# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0022_auto_20171119_0421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchinterest',
            name='faculty',
        ),
        migrations.AlterModelOptions(
            name='achievement',
            options={'ordering': ['year']},
        ),
        migrations.AlterModelOptions(
            name='administrativeresponsibility',
            options={'verbose_name_plural': 'Administrative Responsibilities'},
        ),
        migrations.AlterModelOptions(
            name='conference',
            options={'ordering': ['year']},
        ),
        migrations.AlterModelOptions(
            name='journal',
            options={'ordering': ['year']},
        ),
        migrations.AlterModelOptions(
            name='professionalexperience',
            options={'ordering': ['duration']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['duration']},
        ),
        migrations.RemoveField(
            model_name='administrativeresponsibility',
            name='end_month',
        ),
        migrations.RemoveField(
            model_name='administrativeresponsibility',
            name='end_year',
        ),
        migrations.RemoveField(
            model_name='administrativeresponsibility',
            name='start_month',
        ),
        migrations.RemoveField(
            model_name='administrativeresponsibility',
            name='start_year',
        ),
        migrations.RemoveField(
            model_name='professionalexperience',
            name='end_year',
        ),
        migrations.RemoveField(
            model_name='professionalexperience',
            name='start_year',
        ),
        migrations.AddField(
            model_name='administrativeresponsibility',
            name='end',
            field=models.CharField(blank=True, default='Present', max_length=20, verbose_name='Till'),
        ),
        migrations.AddField(
            model_name='administrativeresponsibility',
            name='start',
            field=models.CharField(default='Jan 2017', max_length=20, verbose_name='From'),
        ),
        migrations.AddField(
            model_name='professionalexperience',
            name='duration',
            field=models.CharField(default='2017-Ongoing', max_length=20),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='year',
            field=models.IntegerField(default=2017),
        ),
        migrations.AlterField(
            model_name='conference',
            name='event',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='conference',
            name='participants',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='conference',
            name='topic',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='conference',
            name='year',
            field=models.IntegerField(default=2017),
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(default='CS221', max_length=6, verbose_name='Course Code'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Course Name'),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('odd', 'July-Nov'), ('even', 'Jan-May')], max_length=4),
        ),
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.IntegerField(default=2017),
        ),
        migrations.AlterField(
            model_name='journal',
            name='book',
            field=models.CharField(max_length=100, verbose_name='Published In'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='contributors',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='journal',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='journal',
            name='year',
            field=models.IntegerField(default=2017),
        ),
        migrations.DeleteModel(
            name='ResearchInterest',
        ),
    ]
