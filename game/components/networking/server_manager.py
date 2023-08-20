from game.ecs import Component
from game.networking import Server
from game.networking.events import TilesetUpdated, ActorSpawned, PlayerAssigned
from ..tiles import TilesetPhysics
from ..actor import Player
from ..physics import Position
from . import Networked, ServerPlayer
from game.utils import Vector

class ConnectHandler:
  def __init__(self, server_manager):
    self.server_manager = server_manager

  def handle_connect(self, server, id):
    #TODO: maybe make Tileset its own component that physics and baked both require?
    # that would make it harder to "change" the tileset without just destroying the entity but idk
    ts = self.server_manager.entity.world.find_component(TilesetPhysics).tileset
    server.send(id, TilesetUpdated(ts))

    #TODO: create player (this maybe should be a separate handler)
    world = self.server_manager.entity.world
    world.create_entity([
      Networked(id),
      Position(Vector(2, 2)), #TODO: hardcoded position
      ServerPlayer(server)
    ])
    #tell the player he controls the newly spawned actor
    server.send(id, PlayerAssigned(id))

class ServerManager(Component):
  def __init__(self):
    super().__init__()
    self.queue = []
    self.server = None
    self.networked_entities = {}

  def spawn(self, entity):
    id = entity.get_component(Networked).id
    self.networked_entities[id] = entity
    #TODO: send spawned event (would require networking other entities, not just actor)

  def despawn(self, entity):
    id = entity.get_component(Networked).id
    del self.networked_entities[id]
    #TODO: send spawned event (would require networking other entities, not just actor)

  def start(self):
    #TODO: circular imports
    from game.networking.commands import PlayerMoveHandler, \
      PlayerUseSkillHandler

    #TODO: i guess here is as good a place as any to register some handlers
    self.server = Server(
      connect_handlers=[ConnectHandler(self)],
      command_handlers=[
        PlayerMoveHandler(self),
        PlayerUseSkillHandler(self),
      ],
    )
    self.server.start()
