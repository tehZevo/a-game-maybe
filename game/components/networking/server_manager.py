from game.ecs import Component
from game.utils.networking import Server, TestClient

WARN_MESSAGES = 1000

class ServerManager(Component):
  def __init__(self):
    super().__init__()
    self.queue = []
    self.server = None

  def start(self):
    # create_server(add_to_queue)
    self.server = Server(self.on_connect, self.on_disconnect, self.on_message)
    self.server.start()

    TestClient().connect()

  def on_connect(self, id):
    print(id, "connected")
    self.server.send(id, f"hello, {id}")

  def on_disconnect(self, id):
    print(id, "disconnected")

  def on_message(self, id, message):
    #TODO: block when too many messages on queue?
    #TODO: handle ids
    #TODO: use Queue
    self.queue.append(message)
    if len(self.queue) > WARN_MESSAGES:
      print(f"Warning, {len(self.queue)} messages on the server queue!")

  def update(self):
    while len(self.queue) > 0:
      message = self.queue.pop(0)
      print("handling", message)
