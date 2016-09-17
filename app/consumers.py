from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session, enforce_ordering


@channel_session
@enforce_ordering
def ws_connect(message):
    """
    Connected to websocket.connect channel

    Todo: check if there is a user, if yes, add to room.
    Todo: get room id
    """
    room = message.content['path'].strip("/")
    print(room)
    Group("room-%s" % room).add(message.reply_channel)
    Group("room-%s" % room).send("test")
    print("blubb")
    print("connection to %s" % room)
    message.channel_session['room'] = room
    Group("room-%s" % room).add(message.reply_channel)
    Group("room-%s" % room).send("user joined chat-%s" % room)
    print("user joined chat-%s" % room)


@channel_session
@enforce_ordering
def ws_disconnect(message):
    """
    Connected to websocket.disconnect channel

    Todo: check if there is a user, if yes, remove from room.
    """
    Group("room-%s" % message.channel_session['room']).discard(message.reply_channel)
    Group("room-%s" % room).send("user left chat-%s" % room)
    print("user left chat-%s" % room)


@channel_session
@enforce_ordering
def ws_message(message):
    """
    Connected to websocket.receive channel

    Todo: 
    """
    Group("room-%s" % message.channel_session['room']).send({"text": message['text']})

"""        
    ChatMessage.objects.create(
        room=room,
        text=message.content['message'],
        user=user,
    )
"""

