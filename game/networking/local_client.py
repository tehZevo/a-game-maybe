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

  async def handle_messages(self):
    for message in self.connection.receive_all():
      self.on_message(message)

  def send(self, command):
    self.connection.send(self.build_command(command))

  def disconnect(self):
    raise NotImplementedError