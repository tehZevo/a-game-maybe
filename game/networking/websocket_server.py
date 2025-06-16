from threading import Thread
import uuid
from enum import Enum

from websockets.sync.server import serve
from websockets.exceptions import ConnectionClosed

from .server import Server

class WebsocketServer(Server):
  def __init__(self, connect_handlers=[], disconnect_handlers=[], command_handlers=[]):
    super().__init__(connect_handlers, disconnect_handlers, command_handlers)

  def start(self, host="localhost", port=8765):
    def coro():
      def connection_handler(websocket):
        #generate a uuid for the client and call on connect
        id = str(uuid.uuid4())
        self.on_connect(id, websocket)

        #listen for messages until client disconnects
        try:
          for message in websocket:
            self.on_message(id, message)
        except ConnectionClosed as e:
          print("failed recieve from client: disconnected")
          self.on_disconnect(id)

        #TODO: is it possible to get here without experiencing ConnectionClosed?
        #call on disconnect with client's id
        self.on_disconnect(id)

      with serve(connection_handler, host, port) as server:
        server.serve_forever() #o7

    t = Thread(target=coro, daemon=True)
    t.start()

  def send(self, id, event):
    try:
      self.clients[id].send(self.build_event(event))
    except ConnectionClosed as e:
      print("failed to send to client: disconnected")
      self.on_disconnect(id)
    except KeyError as e:
      print("already disconnected client", id, event)
