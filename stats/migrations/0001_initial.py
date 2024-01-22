# Generated by Django 3.0.7 on 2020-11-07 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('codegnan', '0027_release_0_28_0'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_time', models.CharField(default='00:00:00', max_length=100)),
                ('video_duration', models.CharField(default='00:00:00', max_length=100)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codegnan.Course')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codegnan.Lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'course', 'lesson')},
            },
        ),
        migrations.CreateModel(
            name='LessonLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_access_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.TrackLesson')),
            ],
        ),
    ]
