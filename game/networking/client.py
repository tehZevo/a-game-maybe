from enum import Enum
from collections import defaultdict
from queue import Queue, Empty
import json

import dacite

dacite_config = dacite.Config(cast=[Enum])

class Client:
  def __init__(self):
    self.events = Queue()

  def setup_handlers(self, connect_handlers=[], disconnect_handlers=[], event_handlers=[]):
    self.connect_handlers = connect_handlers
    self.disconnect_handlers = disconnect_handlers
    self.event_handlers = defaultdict(list)
    self.event_types = {}
    for handler in event_handlers:
      self.register_event_handler(handler)

  async def connect(self):
    raise NotImplementedError
  
  def send(self, command):
    raise NotImplementedError
  
  def disconnect(self):
    raise NotImplementedError
  
  #TODO: pass client manager or game here?
  def handle_events(self):
    while True:
      try:
        event = self.events.get_nowait()
        #tell all handlers about command
        for handler in self.event_handlers[event.__class__]:
          handler.handle(self.client_manager, self, event)
      except Empty:
        break
  
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
    #construct event and add to queue
    message = json.loads(message)
    event_type = self.event_types[message["type"]]
    event = dacite.from_dict(event_type, message["data"], config=dacite_config)
    self.events.put(event)

  def build_command(self, command):
    command_type = command.__class__.__name__
    command = {
      "type": command_type,
      "data": command
    }
    return json.dumps(command, default=lambda o: o.__dict__)
