import asyncio
import random

from .client import Client

class LocalClient(Client):
  def __init__(self):
    super().__init__()
    self.connection = None

  async def connect(self, server):
    self.connection = server.connect(self)
    self.on_connect()

  def send(self, command):
    self.connection.send(self.build_command(command))