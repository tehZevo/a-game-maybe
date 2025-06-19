from enum import Enum
from collections import defaultdict
from queue import Queue, Empty
import json

import dacite

dacite_config = dacite.Config(cast=[Enum])

class Server:
  def __init__(self):
    self.clients = {}
    self.server_manager = None
    self.commands = Queue()
    #TODO: track events per second sent/received

  def setup_handlers(self, connect_handlers=[], disconnect_handlers=[], command_handlers=[]):
    self.connect_handlers = connect_handlers
    self.disconnect_handlers = disconnect_handlers
    self.command_handlers = defaultdict(list)
    self.command_types = {}
    for handler in command_handlers:
      self.register_command_handler(handler)

  def start(self):
    raise NotImplementedError
  
  def send(self, id, event):
    raise NotImplementedError
  
  #TODO: pass server manager or game here?
  def handle_commands(self):
    while True:
      try:
        (client_id, command) = self.commands.get_nowait()
        #tell all handlers about command
        for handler in self.command_handlers[command.__class__]:
          handler.handle(self.server_manager, self, client_id, command)
      except Empty: 
        break
  
  def register_command_handler(self, handler):
    #add handler to list of handlers for given event type
    self.command_handlers[handler.command_type].append(handler)
    #store command type for quick retrieval
    self.command_types[handler.command_type.__name__] = handler.command_type

  def on_connect(self, id, connection):
    """Call me with an id and connection object of your choice"""
    #store connection and tell handlers about connection
    self.clients[id] = connection
    for handler in self.connect_handlers:
      handler.handle_connect(self.server_manager, self, id)

  def on_disconnect(self, id):
    #forget connection and tell handlers about disconnect
    try:
      del self.clients[id]
      for handler in self.disconnect_handlers:
        handler(self, id)
    except KeyError as e:
      print("client already disconnected", id)

  def on_message(self, id, message):
    #construct command and add to queue
    message = json.loads(message)
    command_type = self.command_types[message["type"]]
    command = dacite.from_dict(command_type, message["data"], config=dacite_config)
    self.commands.put((id, command))

  def build_event(self, event):
    event_type = event.__class__.__name__
    event = {
      "type": event_type,
      "data": event
    }
    return json.dumps(event, default=lambda o: o.__dict__)

  def broadcast(self, event):
    for id in list(self.clients.keys()):
      self.send(id, event)
