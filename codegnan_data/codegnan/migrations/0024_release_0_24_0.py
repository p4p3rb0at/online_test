# Generated by Django 3.0.7 on 2020-09-14 10:45

from django.db import migrations, models
import codegnan.models


class Migration(migrations.Migration):

    dependencies = [
        ('codegnan', '0023_release_0_23_0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentupload',
            name='assignmentFile',
            field=models.FileField(max_length=255, upload_to=codegnan.models.get_assignment_dir),
        ),
    ]