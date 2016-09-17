# -*- coding: utf-8 -*-
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings
from django.db import models
import random
import string

def get_random_sessionid():
    """
    Create random sessionid
    """
    session_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    return session_id

class JukeboxUser(models.Model):
    """
    """
    name = models.CharField(max_length=255, blank=True, null=True)
    session_id = models.CharField(max_length=255, default=get_random_sessionid)

    def __unicode__(self):
        return u"{}".format(self.name)


class Rating(models.Model):
    user = models.ForeignKey(JukeboxUser)
    video = models.ForeignKey('Video')
    positive_rating = models.BooleanField()

    def __unicode__(self):
        return u"{} rated {} {}".format(self.user, self.video, self.positive_rating)


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
        return u"{} ({})".format(self.name, self.admin.name)

class Video(models.Model):
    """
    """
    title = models.CharField(max_length=255, verbose_name="Videotitel auf YouTube")
    duration = models.CharField(max_length=255, verbose_name="Dauer des Videos")
    uploader = models.CharField(max_length=255, verbose_name="Uploader auf YouTube")
    url = models.URLField(max_length=255, verbose_name="YouTube URL")
    thumb_url = models.URLField(max_length=255, verbose_name="YouTube Thumbnail URL")
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

    def __unicode__(self):
        return u"{} ({})".format(self.title, self.duration)


class ChatMessage(models.Model):
    user = models.ForeignKey(JukeboxUser)
    datetime = models.DateTimeField(blank=False, null=False, default=timezone.now, verbose_name="Sent")
    text = models.TextField()
    room = models.ForeignKey(Room)

    def __unicode__(self):
        return u"{}@{} schrieb \"\"".format(self.name, self.room, self.text)
    

class UserToRoom(models.Model):
    user = models.ForeignKey(JukeboxUser)
    room = models.ForeignKey(Room)
    datetime_joined = models.DateTimeField(blank=False, null=False, default=timezone.now, verbose_name="Sent")

    def __unicode__(self):
        return u"{} in {}".format(self.user, self.room)