# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-16 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codegnan', '0006_release_0_6_0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='activation_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]