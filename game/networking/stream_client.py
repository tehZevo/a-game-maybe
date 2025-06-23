import time
import asyncio

from .client import Client

class StreamClient(Client):
  def __init__(self, host, port):
    super().__init__()
    self.host = host
    self.port = port
    self.writer = None

  async def connect(self):
    reader, writer = await asyncio.open_connection(self.host, self.port)
    self.writer = writer
    self.on_connect()
    async for message in reader:
      self.on_message(message.decode("utf-8"))
    self.on_disconnect()

  def send(self, message):
    self.writer.write(message.encode("utf-8")+b"\n")

  def disconnect(self):
    self.writer.close()