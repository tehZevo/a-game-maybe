import time
import asyncio

# from websockets.asyncio.client import connect

from .client import Client

class WebsocketClient(Client):
  def __init__(self, ws_url):
    super().__init__()
    self.ws_url = ws_url
    self.ws = None

  async def connect(self):
    async with connect(self.ws_url) as websocket:
      self.ws = websocket
      self.on_connect()
      async for message in websocket:
        self.on_message(message)
    self.on_disconnect()

  def send(self, command):
    asyncio.create_task(self.ws.send(self.build_command(command)))

  def disconnect(self):
    self.ws.close()