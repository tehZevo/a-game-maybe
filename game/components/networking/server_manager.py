from game.ecs import Component
from game.networking import Server
from game.networking.command_handlers import TestCommandHandler

class ServerManager(Component):
  def __init__(self):
    super().__init__()
    self.queue = []
    self.server = None

  def start(self):
    #TODO: i guess here is as good a place as any to register some handlers
    self.server = Server(command_handlers=[
      TestCommandHandler()
    ])
    self.server.start()
