from game.ecs import Component
from game.networking import Server
from game.networking.events import TilesetUpdated, ActorSpawned
from game.networking.commands import TestCommandHandler
from ..tiles import TilesetPhysics
from ..actor import Player
from ..physics import Position
from . import Id, ServerPlayer
from game.utils import Vector

class ConnectHandler:
  def __init__(self, server_manager):
    self.server_manager = server_manager

  def handle_connect(self, server, id):
    #TODO: maybe make Tileset its own component that physics and baked both require?
    # that would make it harder to "change" the tileset without just destroying the entity but idk
    ts = self.server_manager.entity.world.find_components(TilesetPhysics)[0].tileset
    server.send(id, TilesetUpdated(ts))

    #TODO: create player (this maybe should be a separate handler)
    world = self.server_manager.entity.world
    world.create_entity([
      Id(id),
      Position(Vector(2, 2)), #TODO: hardcoded position
      ServerPlayer(server)
    ])
    server.send(id, ActorSpawned(id))

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
