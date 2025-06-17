import asyncio
import random

from .client import Client

class LocalClient(Client):
  def __init__(self, server):
    super().__init__()
    self.server = server
    self.connection = None

  async def connect(self):
    self.connection = self.server.connect()
    self.on_connect()
    
    while True:
      processed_a_message = False
      for message in self.connection.receive_all():
        self.on_message(message)
        processed_a_message = True
      
      await asyncio.sleep(0)

  def send(self, command):
    self.connection.send(self.build_command(command))

  def disconnect(self):
    raise NotImplementedError