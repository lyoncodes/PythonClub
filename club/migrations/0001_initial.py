# Generated by Django 4.0.1 on 2022-02-04 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('time', models.DateTimeField()),
                ('location', models.TextField(blank=True, null=True)),
                ('agenda', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'meeting',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('URL', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='MeetingMinutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('attendance', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('meetingId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='club.meeting')),
            ],
            options={
                'db_table': 'minute',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.TextField()),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('description', models.TextField()),
                ('userId', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'event',
            },
        ),
    ]