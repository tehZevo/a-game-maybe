import json

from .client_channel import ClientChannel

class Client:
  def __init__(self):
    self.default_channel = ClientChannel(self)
    self.channels = {}
  
  def add_channel(self, channel_id):
    channel = ClientChannel(self, channel_id)
    self.channels[channel_id] = channel
    return channel
  
  def get_channel(self, channel_id):
    return self.channels[channel_id]
  
  def remove_channel(self, channel_id):
    del self.channels[channel_id]

  def handle_events(self):
    self.default_channel.handle_events()

  #NOTE: this creates the default channel
  def setup_handlers(self, connect_handlers=[], disconnect_handlers=[], event_handlers=[]):
    self.connect_handlers = connect_handlers
    self.disconnect_handlers = disconnect_handlers
    self.default_channel.setup_handlers(event_handlers)

  async def connect(self):
    raise NotImplementedError
  
  def send(self, message):
    raise NotImplementedError
  
  def disconnect(self):
    raise NotImplementedError
  
  def on_connect(self):
    #tell handlers about connection
    for handler in self.connect_handlers:
      handler.handle_connect(self)
  
  def on_disconnect(self):
    #tell handlers about disconnect
    for handler in self.disconnect_handlers:
      handler.handle_disconnect(self)
  
  def on_message(self, message):
    message = json.loads(message)
    channel_id = message["channel"]
    
    if channel_id is None:
      self.default_channel.on_message(message)
    elif channel_id in self.channels:
      self.get_channel(channel_id).on_message(message)
    else:
      print(f"[Client] Received event for non existent channel {channel_id}: {event}")
