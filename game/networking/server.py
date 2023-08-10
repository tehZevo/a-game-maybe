from collections import defaultdict
import json

from game.utils.networking import create_ws_server

class Server:
  def __init__(self, connect_handlers=[], disconnect_handlers=[], command_handlers=[]):
    self.clients = {}
    self.connect_handlers = connect_handlers
    self.disconnect_handlers = disconnect_handlers
    self.command_handlers = defaultdict(list)
    self.command_types = {}

    for handler in command_handlers:
      self.register_command_handler(handler)

  def register_command_handler(self, handler):
    #add handler to list of handlers for given event type
    self.command_handlers[handler.command_type].append(handler)
    #store command type for quick retrieval
    self.command_types[handler.command_type.__name__] = handler.command_type

  def start(self, host="localhost", port=8765):
    create_ws_server(self.on_connect, self.on_disconnect, self.on_message, host, port)

  def on_connect(self, id, ws):
    #store websocket and tell handlers about connection
    self.clients[id] = ws
    for handler in self.connect_handlers:
      handler.handle_connect(self, id)

  def on_disconnect(self, id):
    #forget websocket and tell handlers about disconnect
    del self.clients[id]
    for handler in self.disconnect_handlers:
      handler.handle_disconnect(self, id)

  def on_message(self, id, message):
    #parse and read command type
    message = json.loads(message)
    command_type_name = message["type"]
    #construct command
    command = self.command_types[command_type_name](**message["data"])
    #tell all handlers about command
    for handler in self.command_handlers[command.__class__]:
      handler.handle(self, id, command)

  def build_event(self, event):
    event_type = event.__class__.__name__
    event = {
      "type": event_type,
      "data": event.__dict__
    }
    return json.dumps(event)

  def send(self, id, event):
    self.clients[id].send(self.build_event(event))

  def broadcast(self, event):
    event = self.build_event(event)
    for client in self.clients.values():
      client.send(event)
