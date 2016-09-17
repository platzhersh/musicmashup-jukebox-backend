from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group

# Connected to websocket.connect
def ws_connect(message):
    Group("chat").add(message.reply_channel)

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)

# Connected to websocket.receive
def ws_message(message):
    Group("chat").send({
        "text": "[user] %s" % message.content['text'],
    })