from game.ecs import Component
from game.networking import Server
from game.utils import Vector
from ..physics import Position

class ConnectHandler:
  def __init__(self, server_manager):
    self.server_manager = server_manager

  def handle_connect(self, server, id):
    #TODO: circular imports
    from game.networking.events import TilesetUpdated, PlayerAssigned
    from ..tiles import TilesetPhysics
    #TODO: maybe make Tileset its own component that physics and baked both require?
    # that would make it harder to "change" the tileset without just destroying the entity but idk
    ts = self.server_manager.entity.world.find_component(TilesetPhysics).tileset
    server.send(id, TilesetUpdated(ts))

    #TODO: circular import
    from . import Id, ServerPlayer
    #TODO: create player (this maybe should be a separate handler)
    world = self.server_manager.entity.world
    world.create_entity([
      Id(id),
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
    #TODO: circular import
    from . import Id
    id = entity.get_component(Id).id
    self.networked_entities[id] = entity
    #TODO: send spawned event (would require networking other entities, not just actor)

  def despawn(self, entity):
    #TODO: circular import
    from . import Id
    id = entity.get_component(Id).id
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
