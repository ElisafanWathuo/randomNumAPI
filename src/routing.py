from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

from randomNum.bindings import RandomBinding

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
import randomNum.routing

# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             randomNum.routing.websocket_urlpatterns
#         )
#     ),
# })

class APIDemultiplexer(WebsocketDemultiplexer):

    consumers = {
      'random': RandomBinding.consumer
    }

channel_routing = [
    route_class(APIDemultiplexer)
]