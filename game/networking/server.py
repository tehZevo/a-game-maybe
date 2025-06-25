from uuid import uuid4

from collections import defaultdict
from queue import Queue, Empty
import json

from .server_channel import ServerChannel

#TODO: validate that client can talk on channel?

class Server:
  def __init__(self):
    self.default_channel = ServerChannel(self)
    self.channels = {}
    self.clients = {}

  def create_channel(self):
    channel_id = str(uuid4())
    channel = ServerChannel(self, channel_id)
    self.channels[channel_id] = channel
    return channel

  def get_channel(self, channel_id):
    return self.channels[channel_id]
  
  def remove_channel(self, channel_id):
    del self.channels[channel_id]
  
  def handle_commands(self):
    self.default_channel.handle_commands()
    
  def setup_handlers(self, connect_handlers=[], disconnect_handlers=[], command_handlers=[]):
    self.connect_handlers = connect_handlers
    self.disconnect_handlers = disconnect_handlers
    self.default_channel.setup_handlers(command_handlers)

  def start(self):
    raise NotImplementedError
  
  def send(self, id, message):
    raise NotImplementedError
  
  def on_connect(self, id, connection):
    """Call me with an id and connection object of your choice"""
    #store connection and tell handlers about connection
    self.clients[id] = connection
    self.default_channel.clients.add(id)
    for handler in self.connect_handlers:
      handler(id)

  def on_disconnect(self, id):
    #forget connection and tell handlers about disconnect
    try:
      del self.clients[id]
      for handler in self.disconnect_handlers:
        handler(id)
      for channel in self.channels.values():
        channel.clients.remove(id)
    except KeyError as e:
      # print("[Server] Client already disconnected", id)
      pass
    #remove client from all channels
    except Exception as e:
      print(e)

  def on_message(self, client_id, message):
    message = json.loads(message)
    channel_id = message["channel"]

    channel = self.default_channel if channel_id is None else self.channels.get(channel_id)
    if channel is None:
      print(f"[Server] Received command for non existent channel {channel_id}: {message}")
      return
    
    #NOTE: verifies if client is in channel
    if client_id not in channel.clients:
      print(f"[Server] Client {client_id} tried to send a command to a channel he's not in: {channel_id}, {message}")
      return

    channel.on_message(client_id, message)