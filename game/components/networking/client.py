from game.ecs import Component
from ._server import start_server

WARN_MESSAGES = 1000


class Client(Component):
  def __init__(self):
    super().__init__()
    #TODO: warn when too many messages on queue, or maybe block?
    self.queue = []

  def start(self):
    def add_to_queue(message):
      self.queue.append(message)
      if len(self.queue) > WARN_MESSAGES:
        print(f"Warning, {len(self.queue)} messages on the server queue!")

    # start_server(add_to_queue)

  def update(self):
    for message in self.queue:
