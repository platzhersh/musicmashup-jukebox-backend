# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 04:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jukebox', '0003_auto_20160917_0544'),
    ]

    operations = [
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
            model_name='room',
            name='datetime_closed',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Closed'),
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
