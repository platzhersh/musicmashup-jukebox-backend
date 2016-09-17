# -*- coding: utf-8 -*-
from django.contrib import admin
from jukebox.models import Room, Video, JukeboxUser, Rating, ChatMessage, UserToRoom


admin.site.register(Room)
admin.site.register(Video)
admin.site.register(JukeboxUser)
admin.site.register(Rating)
admin.site.register(ChatMessage)
admin.site.register(UserToRoom)
