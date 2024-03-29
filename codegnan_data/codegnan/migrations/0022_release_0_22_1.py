# Generated by Django 3.0.7 on 2020-08-28 07:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codegnan', '0021_auto_20200703_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_enroll_time',
            field=models.DateTimeField(default=datetime.datetime(2199, 1, 1, 0, 0, tzinfo=utc), null=True, verbose_name='End Date and Time for enrollment of course'),
        ),
        migrations.AlterField(
            model_name='questionpaper',
            name='fixed_question_order',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='end_date_time',
            field=models.DateTimeField(default=datetime.datetime(2199, 1, 1, 0, 0, tzinfo=utc), null=True, verbose_name='End Date and Time of the quiz'),
        ),
    ]
