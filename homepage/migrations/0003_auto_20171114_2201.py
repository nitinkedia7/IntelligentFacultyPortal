# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_faculty_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department',
            field=models.CharField(choices=[('bsbe', 'Biosciences and Bioengineering'), ('chem', 'Chemistry'), ('ce', 'Chemical Engineering'), ('civil', 'Civil Engineering'), ('des', 'Design'), ('cse', 'Computer Science and Engineering'), ('eee', 'Electronics and Electrical Engineering'), ('hss', 'Humanities and Social Sciences'), ('phy', 'Physics'), ('math', 'Mathematics'), ('mech', 'Mechanical Engineering')], max_length=6),
        ),
    ]
