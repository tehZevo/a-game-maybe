from threading import Thread
import uuid

from websockets.sync.server import serve
from websockets.sync.client import connect

def create_ws_server(on_connect, on_disconnect, on_message, host="localhost", port=8765):
  def coro():
    def connection_handler(websocket):
      #generate a uuid for the client and call on connect
      id = str(uuid.uuid4())
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

def create_ws_client(on_connect, on_disconnect, on_message, host="localhost", port=8765):
  def coro():
    #TODO: allow wss://
    with connect(f"ws://{host}:{port}") as websocket:
      on_connect(websocket)
      for message in websocket:
        on_message(message)
    on_disconnect()

  t = Thread(target=coro, daemon=True)
  t.start()
