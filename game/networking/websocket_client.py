from threading import Thread

from websockets.sync.client import connect

from .client import Client

class WebsocketClient(Client):
  def __init__(self, ws_url):
    super().__init__()
    self.ws_url = ws_url
    self.ws = None

  def connect(self):
    def coro():
      with connect(self.ws_url) as websocket:
        self.ws = websocket
        self.on_connect()
        for message in websocket:
          self.on_message(message)
      self.on_disconnect()

    t = Thread(target=coro, daemon=True)
    t.start()

  def send(self, command):
    self.ws.send(self.build_command(command))

  def disconnect(self):
    self.ws.close()