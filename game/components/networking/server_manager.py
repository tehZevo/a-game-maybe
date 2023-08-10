from game.ecs import Component
from ..graphics import BakedTileset
from game.networking import Server
from game.networking.events import TilesetUpdated
from game.networking.commands import TestCommandHandler

class ConnectHandler:
  def __init__(self, server_manager):
    self.server_manager = server_manager

  def handle_connect(self, server, id):
    ts = self.server_manager.entity.world.find_components(BakedTileset)[0].tileset
    server.send(id, TilesetUpdated(ts))

class ServerManager(Component):
  def __init__(self):
    super().__init__()
    self.queue = []
    self.server = None

  def start(self):
    #TODO: i guess here is as good a place as any to register some handlers
    self.server = Server(
      connect_handlers=[ConnectHandler(self)],
      command_handlers=[
        TestCommandHandler()
      ],
    )
    self.server.start()
