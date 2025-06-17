import asyncio
import uuid

from .server import Server

class StreamServer(Server):
  def __init__(self, host="localhost", port=8765):
    super().__init__()
    self.host = host
    self.port = port

  async def start(self):
    async def connection_handler(reader, writer):
      #generate a uuid for the client and call on connect
      id = str(uuid.uuid4())
      self.on_connect(id, writer)
      async for message in reader:
        self.on_message(id, message.decode("utf-8"))
      self.on_disconnect(id)

    await asyncio.start_server(connection_handler, self.host, self.port) #o7

  def send(self, id, event):
    writer = self.clients[id]
    writer.write(self.build_event(event).encode("utf-8")+b"\n")
