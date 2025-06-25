import traceback
from enum import Enum
from collections import defaultdict
from queue import Queue, Empty
import json

import dacite

dacite_config = dacite.Config(cast=[Enum])

class ServerChannel:
  def __init__(self, server, id=None):
    self.server = server
    self.id = id
    self.commands = Queue()
    self.clients = set()
  
  def build_event(self, event, id):
    event_type = event.__class__.__name__
    event = {
      "channel": id,
      "type": event_type,
      "data": event
    }
    return json.dumps(event, default=lambda o: o.__dict__)
  
  def send(self, client_id, event):
    if self.id is not None and self.id not in self.server.channels:
      print("trying to send to closed channel", self.id)
    event = self.build_event(event, self.id)
    self.server.send(client_id, event)
  
  def on_message(self, client_id, message):
    command_type = self.command_types[message["type"]]
    command = dacite.from_dict(command_type, message["data"], config=dacite_config)
    self.commands.put((client_id, command))
  
  def broadcast(self, event):
    for id in list(self.clients):
      self.send(id, event)
  
  def setup_handlers(self, handlers=[]):
    self.handlers = defaultdict(list)
    self.command_types = {}
    for handler in handlers:
      self.register_command_handler(handler)
  
  def register_command_handler(self, handler):
    self.handlers[handler.command_type].append(handler)
    self.command_types[handler.command_type.__name__] = handler.command_type

  def handle_commands(self):
    while True:
      try:
        (client_id, command) = self.commands.get_nowait()
        for handler in self.handlers[command.__class__]:
          handler.handle(client_id, command)
      except Empty: 
        break
      except Exception:
        print(traceback.format_exc())