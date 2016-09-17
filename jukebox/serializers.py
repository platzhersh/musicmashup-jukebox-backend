# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from jukebox.models import Room


class VideoSerializer(serializers.ModelSerializer):
    """
    """
    rating = serializers.ReadOnlyField(source='get_rating')
    class Meta:
        model = Video