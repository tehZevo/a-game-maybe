import asyncio
import uuid

from .server import Server

class LocalConnection:
  def __init__(self, server, id):
    self.server = server
    self.id = id
  
  def send(self, message):
    self.server.on_message(self.id, message)

class LocalServer(Server):
  def __init__(self):
    super().__init__()
  
  def connect(self, client):
    id = str(uuid.uuid4())
    self.on_connect(id, client)
    return LocalConnection(self, id)
  
  async def start(self):
    return

  def send(self, id, event):
    self.clients[id].on_message(self.build_event(event))
