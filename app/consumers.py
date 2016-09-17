from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session, enforce_ordering
import os
import random
import string
from jukebox.models import JukeboxUser

@channel_session
@enforce_ordering(slight=True)
def ws_connect(message):
    """
    Connected to websocket.connect channel

    Todo: create a user and store session_id
    """
    room = os.path.basename(os.path.normpath(message.content['path']))
    message.channel_session['room'] = room
    session_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    message.channel_session['session_id'] = session_id
    
    user = JukeboxUser.objects.create(
    	name=session_id,
    	session_id=session_id,
    	room_id=room)
    
    message.channel_session['user_id'] = user.id
    message.channel_session['user_name'] = user.name

    Group("room-%s" % room).add(message.reply_channel)  
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

