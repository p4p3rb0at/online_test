# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2020-02-05 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codegnan', '0015_release_0_10_0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='language',
            field=models.CharField(choices=[('python', 'Python'), ('bash', 'Bash'), ('c', 'C Language'), ('cpp', 'C++ Language'), ('java', 'Java Language'), ('scilab', 'Scilab'), ('r', 'R')], max_length=24),
        ),
    ]
