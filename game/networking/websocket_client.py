from threading import Thread

from websockets.sync.client import connect

from .client import Client

class WebsocketClient(Client):
  def __init__(self, connect_handlers=[], disconnect_handlers=[], event_handlers=[]):
    super().__init__(connect_handlers, disconnect_handlers, event_handlers)
    self.ws = None

  def connect(self, host="localhost", port=8765):
    def coro():
      #TODO: allow wss://
      with connect(f"ws://{host}:{port}") as websocket:
        self.on_connect(websocket)
        for message in websocket:
          self.on_message(message)
      self.on_disconnect()

    t = Thread(target=coro, daemon=True)
    t.start()

  def on_connect(self, ws):
    self.ws = ws
    #TODO: this feels weird
    super().on_connect()

  def send(self, command):
    self.ws.send(self.build_command(command))

  def disconnect(self):
    self.ws.close()