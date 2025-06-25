import asyncio
import uuid
import sys

#pygame guard
if sys.platform != "emscripten":
  import importlib
  server = importlib.import_module("websockets.asyncio.server")
  serve = getattr(server, "serve")
  ws_exc = importlib.import_module("websockets.exceptions")
  ConnectionClosed = getattr(ws_exc, "ConnectionClosed")

from .server import Server

class WebsocketServer(Server):
  def __init__(self, host="localhost", port=8765):
    super().__init__()
    self.host = host
    self.port = port

  async def start(self):
    async def connection_handler(websocket):
      #generate a uuid for the client and call on connect
      id = str(uuid.uuid4())
      self.on_connect(id, websocket)

      #listen for messages until client disconnects
      try:
        async for message in websocket:
          self.on_message(id, message)
      except ConnectionClosed as e:
        print("failed recieve from client: disconnected")
        self.on_disconnect(id)
      
      self.on_disconnect(id)

    server = await serve(connection_handler, self.host, self.port)
    await server.serve_forever() #o7

  def send(self, id, message):
    async def inner(message):
      try:
        await self.clients[id].send(message)
      except ConnectionClosed as e:
        print(f"[Server] Failed to send to client {id}: disconnected")
        self.on_disconnect(id)
      except KeyError as e:
        print(f"[Server] Failed to send to client {id}: disconnected")
      except Exception as e:
        print(e)
    asyncio.create_task(inner(message))
