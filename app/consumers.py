from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session, enforce_ordering
import os

@channel_session
@enforce_ordering(slight=True)
def ws_connect(message):
    """
    Connected to websocket.connect channel

    Todo: check if there is a user, if yes, add to room.
    """
    room = os.path.basename(os.path.normpath(message.content['path']))
    message.channel_session['room'] = room
    
    Group("room-%s" % room).add(message.reply_channel)  
    Group("room-%s" % room).send({"text": "Willkommen im Raum %s" % room})
    


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
    Group("room-%s" % room).send("user left chat-%s" % room)
    #print("user left chat-%s" % room)
	


@channel_session
@enforce_ordering
def ws_message(message):
    """
    Connected to websocket.receive channel

    Todo: 
    """
    #Group("room").send({"text": text })
    Group("room-%s" % message.channel_session['room']).send({"text": message['text']})

"""        
    ChatMessage.objects.create(
        room=room,
        text=message.content['message'],
        user=user,
    )
"""

