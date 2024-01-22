# Generated by Django 3.0.7 on 2021-01-12 05:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codegnan', '0027_release_0_28_0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_enroll_time',
            field=models.DateTimeField(default=datetime.datetime(2198, 12, 31, 18, 7, tzinfo=utc), null=True, verbose_name='End Date and Time for enrollment of course'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='end_date_time',
            field=models.DateTimeField(default=datetime.datetime(2198, 12, 31, 18, 7, tzinfo=utc), null=True, verbose_name='End Date and Time of the quiz'),
        ),
    ]
