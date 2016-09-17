# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jukebox', '0006_auto_20160917_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='jukeboxuser',
            name='room_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jukeboxuser',
            name='session_id',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jukebox.JukeboxUser'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jukebox.JukeboxUser'),
        ),
        migrations.AlterField(
            model_name='room',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jukebox.JukeboxUser'),
        ),
        migrations.AlterField(
            model_name='usertoroom',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jukebox.JukeboxUser'),
        ),
        migrations.AlterField(
            model_name='video',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jukebox.JukeboxUser'),
        ),
    ]
