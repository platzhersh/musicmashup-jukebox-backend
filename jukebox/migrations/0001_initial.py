# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Sent')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JukeBoxUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive_rating', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jukebox.JukeBoxUser')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'Name des Kantons')),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Created')),
                ('datetime_closed', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Closed')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name=b'Breitengrad')),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name=b'L\xc3\xa4ngengrad')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jukebox.JukeBoxUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserToRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Sent')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jukebox.Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jukebox.JukeBoxUser')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=255, null=True, verbose_name=b'YouTube Url')),
                ('datetime_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Added')),
                ('played', models.BooleanField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jukebox.Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jukebox.JukeBoxUser')),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jukebox.Video'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jukebox.Room'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jukebox.JukeBoxUser'),
        ),
    ]
