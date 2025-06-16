from threading import Thread
import uuid
from enum import Enum
from collections import defaultdict
import json

import dacite

from websockets.sync.server import serve
from websockets.exceptions import ConnectionClosed
#TODO: make abstract to support other transports like direct in memory and js (for embedding as browser game)

class Server:
  def __init__(self, connect_handlers=[], disconnect_handlers=[], command_handlers=[]):
    self.clients = {}
    self.connect_handlers = connect_handlers
    self.disconnect_handlers = disconnect_handlers
    self.command_handlers = defaultdict(list)
    self.command_types = {}
    self.server_manager = None
    #TODO: track events per second sent/received
    self.one_second = 0
    self.events_per_second = 0

    for handler in command_handlers:
      self.register_command_handler(handler)

  def register_command_handler(self, handler):
    #add handler to list of handlers for given event type
    self.command_handlers[handler.command_type].append(handler)
    #store command type for quick retrieval
    self.command_types[handler.command_type.__name__] = handler.command_type

  def start(self, host="localhost", port=8765):
    def coro():
      def connection_handler(websocket):
        #generate a uuid for the client and call on connect
        id = str(uuid.uuid4())
        self.on_connect(id, websocket)

        #listen for messages until client disconnects
        try:
          for message in websocket:
            self.on_message(id, message)
        except ConnectionClosed as e:
          print("failed recieve from client: disconnected")
          self.on_disconnect(id)

        #call on disconnect with client's id
        self.on_disconnect(id)

      with serve(connection_handler, host, port) as server:
        server.serve_forever() #o7

    t = Thread(target=coro, daemon=True)
    t.start()

  def on_connect(self, id, ws):
    #store websocket and tell handlers about connection
    self.clients[id] = ws
    for handler in self.connect_handlers:
      handler.handle_connect(self.server_manager, self, id)

  def on_disconnect(self, id):
    #forget websocket and tell handlers about disconnect
    try:
      del self.clients[id]
      for handler in self.disconnect_handlers:
        handler(self, id)
    except KeyError as e:
      print("client already disconnected", id)

  def on_message(self, id, message):
    #parse and read command type
    message = json.loads(message)
    command_type_name = message["type"]
    #construct command
    command = dacite.from_dict(self.command_types[command_type_name], message["data"], config=dacite.Config(cast=[Enum]))
    #tell all handlers about command
    for handler in self.command_handlers[command.__class__]:
      handler.handle(self.server_manager, self, id, command)

  def build_event(self, event):
    event_type = event.__class__.__name__
    event = {
      "type": event_type,
      "data": event
    }
    return json.dumps(event, default=lambda o: o.__dict__)

  def send(self, id, event):
    try:
      self.clients[id].send(self.build_event(event))
      self.events_per_second += 1
    except ConnectionClosed as e:
      print("failed to send to client: disconnected")
      self.on_disconnect(id)
    except KeyError as e:
      print("already disconnected client", id, event)

  def broadcast(self, event):
    for id in list(self.clients.keys()):
      self.send(id, event)
