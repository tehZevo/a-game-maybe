import asyncio
import uuid

# from websockets.asyncio.server import serve
# from websockets.exceptions import ConnectionClosed

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

      #TODO: is it possible to get here without experiencing ConnectionClosed?
      #call on disconnect with client's id
      self.on_disconnect(id)

    server = await serve(connection_handler, self.host, self.port)
    await server.serve_forever() #o7

  def send(self, id, event):
    try:
      asyncio.create_task(self.clients[id].send(self.build_event(event)))
    except ConnectionClosed as e:
      print("failed to send to client: disconnected")
      self.on_disconnect(id)
    except KeyError as e:
      print("already disconnected client", id, event)
