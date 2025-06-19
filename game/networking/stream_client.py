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
    print("connecting...")
    while True:
      try:
        reader, writer = await asyncio.open_connection(self.host, self.port)
      except BlockingIOError:
        print("BlockingIOError, sleeping...")
        await aio.sleep(1)
    print("connected")
    reader, writer = await asyncio.open_connection(self.host, self.port)
    self.writer = writer
    self.on_connect()
    async for message in reader:
      self.on_message(message.decode("utf-8"))
    self.on_disconnect()

  def send(self, command):
    self.writer.write(self.build_command(command).encode("utf-8")+b"\n")

  def disconnect(self):
    self.writer.close()