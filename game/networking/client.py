from collections import defaultdict
import json

from game.utils.networking import create_ws_client

class Client:
  def __init__(self, connect_handlers=[], disconnect_handlers=[], event_handlers=[]):
    self.ws = None
    self.connect_handlers = connect_handlers
    self.disconnect_handlers = disconnect_handlers
    self.event_handlers = defaultdict(list)
    self.event_types = {}

    for handler in event_handlers:
      self.register_event_handler(handler)

  def register_event_handler(self, handler):
    #add handler to list of handlers for given event type
    self.event_handlers[handler.event_type].append(handler)
    #store event type for quick retrieval
    self.event_types[handler.event_types.__name__] = handler.event_types

  def connect(self, host="localhost", port=8765):
    create_ws_client(self.on_connect, self.on_disconnect, self.on_message, host, port)

  def on_connect(self, ws):
    #store websocket and tell handlers about connection
    self.ws = ws
    for handler in self.connect_handlers:
      handler.handle_connect(self)

  def on_disconnect(self):
    #tell handlers about disconnect
    for handler in self.disconnect_handlers:
      handler.handle_disconnect(self)

  def on_message(self, message):
    #parse and read event type
    message = json.reads(message)
    event_type = message["type"]
    #construct event
    event = self.event_types[event_type](**message["data"])

    #tell all handlers about event
    for handler in self.event_handlers[event_type]:
      handler.handle(server, event)

  def build_command(self, command):
    command_type = command.__class__.__name__
    command = {
      "type": command_type,
      "data": command.__dict__
    }
    return json.dumps(command)

  def send(self, command):
    self.ws.send(self.build_command(command))

  def disconnect(self):
    self.ws.close()
