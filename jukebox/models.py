# -*- coding: utf-8 -*-
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings
from django.db import models


class JukeBoxUser(models.Model):
    name = models.CharField(max_length=255)


class Room(models.Model):
    """
    TODO: delete
    """
    name = models.CharField(blank=False, null=False, max_length=255, verbose_name="Name des Kantons")
    admin = models.ForeignKey(JukeBoxUser)
    datetime_created = models.DateTimeField(blank=False, null=False, default=timezone.now, verbose_name="Created")
    datetime_closed = models.DateTimeField(blank=False, null=False, default=timezone.now, verbose_name="Closed")
    latitude = models.DecimalField(blank=True, null=True, verbose_name='Breitengrad', max_digits=9, decimal_places=6)
    longitude = models.DecimalField(blank=True, null=True, verbose_name='Längengrad', max_digits=9, decimal_places=6)
    
    def __unicode__(self):
        return u"{}".format(self.name)

class Video(models.Model):
    """
    """
    url = models.URLField(blank=True, null=True, max_length=255, verbose_name="YouTube Url")
    datetime_added = models.DateTimeField(blank=False, null=False, default=timezone.now, verbose_name="Added")
    room = models.ForeignKey(Room)
    user = models.ForeignKey(JukeBoxUser)
    played = models.BooleanField()


class Rating(models.Model):
    user = models.ForeignKey(JukeBoxUser)
    video = models.ForeignKey(Video)
    positive_rating = models.BooleanField()


class ChatMessage(models.Model):
    user = models.ForeignKey(JukeBoxUser)
    datetime = models.DateTimeField(blank=False, null=False, default=timezone.now, verbose_name="Sent")
    text = models.TextField()
    room = models.ForeignKey(Room)
    

class UserToRoom(models.Model):
    user = models.ForeignKey(JukeBoxUser)
    room = models.ForeignKey(Room)
    datetime_joined = models.DateTimeField(blank=False, null=False, default=timezone.now, verbose_name="Sent")
