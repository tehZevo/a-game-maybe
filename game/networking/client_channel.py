import traceback
from enum import Enum
from collections import defaultdict
from queue import Queue, Empty
import json

import dacite

dacite_config = dacite.Config(cast=[Enum])

class ClientChannel:
  def __init__(self, client, id=None):
    self.client = client
    self.id = id
    self.events = Queue()
  
  def build_command(self, command, id):
    command_type = command.__class__.__name__
    command = {
      "channel": id,
      "type": command_type,
      "data": command
    }
    return json.dumps(command, default=lambda o: o.__dict__)
  
  def send(self, command):
    message = self.build_command(command, self.id)
    self.client.send(message)
  
  def on_message(self, message):
    event_type = self.event_types[message["type"]]
    event = dacite.from_dict(event_type, message["data"], config=dacite_config)
    self.events.put(event)

  def setup_handlers(self, handlers=[]):
    self.handlers = defaultdict(list)
    self.event_types = {}
    for handler in handlers:
      self.register_event_handler(handler)
  
  def register_event_handler(self, handler):
    self.handlers[handler.event_type].append(handler)
    self.event_types[handler.event_type.__name__] = handler.event_type

  def handle_events(self):
    while True:
      try:
        event = self.events.get_nowait()
        for handler in self.handlers[event.__class__]:
          handler.handle(event)
      except Empty:
        break
      except Exception:
        print(traceback.format_exc())