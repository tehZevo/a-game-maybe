from enum import Enum
from collections import defaultdict
import json

import dacite

class Client:
  def __init__(self):
    pass

  def setup_handlers(self, connect_handlers=[], disconnect_handlers=[], event_handlers=[]):
    self.connect_handlers = connect_handlers
    self.disconnect_handlers = disconnect_handlers
    self.event_handlers = defaultdict(list)
    self.event_types = {}
    for handler in event_handlers:
      self.register_event_handler(handler)

  def connect(self):
    raise NotImplementedError
  
  def send(self, command):
    raise NotImplementedError
  
  def disconnect(self):
    raise NotImplementedError
  
  def register_event_handler(self, handler):
    #add handler to list of handlers for given event type
    self.event_handlers[handler.event_type].append(handler)
    #store event type for quick retrieval
    self.event_types[handler.event_type.__name__] = handler.event_type

  def on_connect(self):
    #tell handlers about connection
    for handler in self.connect_handlers:
      handler.handle_connect(self)
  
  def on_disconnect(self):
    #tell handlers about disconnect
    for handler in self.disconnect_handlers:
      handler.handle_disconnect(self)
  
  def on_message(self, message):
    #parse and read event type
    message = json.loads(message)
    event_type_name = message["type"]
    #construct event
    event = dacite.from_dict(self.event_types[event_type_name], message["data"], config=dacite.Config(cast=[Enum]))
    #tell all handlers about event
    for handler in self.event_handlers[event.__class__]:
      handler.handle(self.client_manager, self, event)

  def build_command(self, command):
    command_type = command.__class__.__name__
    command = {
      "type": command_type,
      "data": command
    }
    return json.dumps(command, default=lambda o: o.__dict__)
