# TODO: fix package names
from channels.routing import route
from app.consumers import ws_connect, ws_message, ws_disconnect


channel_routing = [
    # You can use a string import path as the first argument as well.
    route("websocket.connect", ws_connect),
    route("websocket.disconnect", ws_disconnect),
    route("websocket.receive", ws_message),
]