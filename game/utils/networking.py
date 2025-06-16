from threading import Thread
from websockets.sync.client import connect

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
