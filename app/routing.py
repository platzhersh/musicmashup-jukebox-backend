# TODO: fix package names
from channels.routing import route
from app.consumers import ws_connect, ws_message, ws_disconnect


channel_routing = [
    route("app.connect", ws_connect),
    route("app.receive", ws_message),
    route("app.disconnect", ws_disconnect),
]