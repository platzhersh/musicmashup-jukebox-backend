# -*- coding: utf-8 -*-
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings
from django.db import models


class JukeboxUser(models.Model):
    name = models.CharField(max_length=255)


class Rating(models.Model):
    user = models.ForeignKey(JukeboxUser)
    video = models.ForeignKey('Video')
    positive_rating = models.BooleanField()


class Room(models.Model):
    """
    """
    name = models.CharField(max_length=255, verbose_name="Raumname")
    admin = models.ForeignKey(JukeboxUser)
    datetime_created = models.DateTimeField(blank=False, null=False, default=timezone.now, verbose_name="Created")
    datetime_closed = models.DateTimeField(blank=True, null=True, verbose_name="Closed")
    latitude = models.DecimalField(blank=True, null=True, verbose_name='Breitengrad', max_digits=9, decimal_places=6)
    longitude = models.DecimalField(blank=True, null=True, verbose_name='Längengrad', max_digits=9, decimal_places=6)
    

    def __unicode__(self):
        return u"{}".format(self.name)

class Video(models.Model):
    """
    """
    url = models.URLField(max_length=255, verbose_name="YouTube URL")
    datetime_added = models.DateTimeField(blank=False, null=False, default=timezone.now, verbose_name="Added")
    room = models.ForeignKey(Room)
    user = models.ForeignKey(JukeboxUser)
    played = models.BooleanField()

    def get_rating(self):
        """
        returns Rating of video
        """
        rating = 0
        ratings = Rating.objects.filter(video__room=self)
        for r in ratings:
            if r.positive_rating:
                rating = rating + 1
            else:
                rating = rating -1 
        return rating


class ChatMessage(models.Model):
    user = models.ForeignKey(JukeboxUser)
    datetime = models.DateTimeField(blank=False, null=False, default=timezone.now, verbose_name="Sent")
    text = models.TextField()
    room = models.ForeignKey(Room)
    

class UserToRoom(models.Model):
    user = models.ForeignKey(JukeboxUser)
    room = models.ForeignKey(Room)
    datetime_joined = models.DateTimeField(blank=False, null=False, default=timezone.now, verbose_name="Sent")
