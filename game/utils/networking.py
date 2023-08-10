from threading import Thread
from queue import Queue
import uuid

from websockets.sync.server import serve
from websockets.sync.client import connect

#TODO: look into the fact that Queue has `block` and `timeout`

class Server:
  #provide callbacks
  def __init__(self, on_connect, on_disconnect, on_message):
    self.clients = {}
    self.on_connect = on_connect
    self.on_disconnect = on_disconnect
    self.on_message = on_message

  def start(self, host="localhost", port=8765):
    create_server(self._on_connect, self._on_disconnect, self.on_message, host, port)

  def _on_connect(self, id, ws):
    self.clients[id] = ws
    self.on_connect(id)

  def _on_disconnect(self, id):
    del self.clients[id]
    self.on_disconnect(id)

  def send(self, id, message):
    self.clients[id].send(message)

  def broadcast(self, message):
    for client in self.clients.values():
      client.send(message)

#TODO: update client to be like server above
class Client:
  def __init__(self):
    self.ws = None

  def connect(self, host="localhost", port=8765):
    create_client(self._on_connect, self.on_disconnect, self.on_message)

  def _on_connect(self, ws):
    self.ws = ws
    self.on_connect()

  def send(self, message):
    self.ws.send(message)

  def disconnect(self):
    self.ws.close()

  def on_connect(self):
    pass

  def on_disconnect(self):
    pass

  def on_message(self):
    pass

def create_server(on_connect, on_disconnect, on_message, host="localhost", port=8765):
  def coro():
    def connection_handler(websocket):
      #generate a uuid for the client and call on connect
      id = uuid.uuid4()
      on_connect(id, websocket)

      #listen for messages until client disconnects
      for message in websocket:
        on_message(id, message)

      #call on disconnect with client's id
      on_disconnect(id)

    with serve(connection_handler, host, port) as server:
      server.serve_forever() #o7

  t = Thread(target=coro, daemon=True)
  t.start()

def create_client(on_connect, on_disconnect, on_message, host="localhost", port=8765):
  def coro():
    #TODO: allow wss://
    with connect(f"ws://{host}:{port}") as websocket:
      on_connect(websocket)
      for message in websocket:
        on_message(message)
    on_disconnect()

  t = Thread(target=coro, daemon=True)
  t.start()
