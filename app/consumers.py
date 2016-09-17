from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session, enforce_ordering
import os
import string
import json
from django.core import serializers
from jukebox.models import JukeboxUser, Video
from django.forms.models import model_to_dict


def get_queue_by_room(room):
    """
    get all queued videos by room that have not been played yet
    """
    data = serializers.serialize("json", Video.objects.filter(room=room, played=False))
    return data

def get_history_by_room(room):
    """
    get all queued videos by room that have already been played
    """
    data = serializers.serialize("json", Video.objects.filter(room=room, played=True))
    return data

def send_initial_data(room, user, message):
    """
    send initial data to new group member
    :room
    :user
    :message
    """
    msg = json.dumps({ 
        "queue": get_queue_by_room(room),
        "user": json.dumps(model_to_dict(user)),
        "history": get_history_by_room(room),
        })
    message.reply_channel.send({ "text" : msg })


@channel_session
@enforce_ordering(slight=True)
def ws_connect(message):
    """
    Connected to websocket.connect channel

    Todo: send current video queue
    """
    room = os.path.basename(os.path.normpath(message.content['path']))
    message.channel_session['room'] = room
    
    # create user
    user = JukeboxUser.objects.create()
    message.channel_session['user_id'] = user.id
    message.channel_session['user_name'] = user.name
    message.channel_session['session_id'] = user.session_id
    
    # send initial data
    send_initial_data(room, user, message)
    

    Group("room-%s" % room).add(message.reply_channel)  

    Group("room-%s" % room).send({"text": "Text"})

    Group("room-%s" % room).send({"text": "Hallo {}, willkommen im Raum {}".format(user.name, room)})


@channel_session
@enforce_ordering
def ws_disconnect(message):
    """
    Connected to websocket.disconnect channel

    Todo: check if there is a user, if yes, remove from room.
    """

    #Group("room").discard(message.reply_channel)
    #Group("room").send("room left")
    room = message.channel_session['room']
    Group("room-%s" % room).discard(message.reply_channel)
    Group("room-%s" % room).send("user left chat-%s" % session_id, room)
    #print("user left chat-%s" % room)
	


@channel_session
@enforce_ordering
def ws_message(message):
    """
    Connected to websocket.receive channel

    Todo: 
    """
    #Group("room").send({"text": text })
    user_name = message.channel_session['user_name']
    room_id = message.channel_session['room']
    msg = "[{}]: {}".format(user_name, message['text'])
    Group("room-%s" % room_id).send({"text": msg })

"""        
    ChatMessage.objects.create(
        room=room,
        text=message.content['message'],
        user=user,
    )
"""

