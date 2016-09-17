# -*- coding: utf-8 -*-
from django.contrib import admin
from jukebox.models import Room, Video, JukeboxUser, Rating, ChatMessage, UserToRoom

class JukeBoxUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'session_id']

admin.site.register(Room)
admin.site.register(Video)
admin.site.register(JukeboxUser, JukeBoxUserAdmin)
admin.site.register(Rating)
admin.site.register(ChatMessage)
admin.site.register(UserToRoom)
