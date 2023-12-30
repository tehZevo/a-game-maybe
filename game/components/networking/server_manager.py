from game.ecs import Component
from game.networking import Server
from game.utils import Vector
import game.components as C

class ConnectHandler:
  def __init__(self, server_manager):
    self.server_manager = server_manager

  def handle_connect(self, server, id):
    #TODO: circular imports
    from game.networking.events import TilesetUpdated, PlayerAssigned
    #TODO: maybe make Tileset its own component that physics and baked both require?
    # that would make it harder to "change" the tileset without just destroying the entity but idk
    ts = self.server_manager.entity.world.find_component(C.TilesetPhysics).tileset
    server.send(id, TilesetUpdated(ts))

    world = self.server_manager.entity.world
    #spawn all other existing for player
    for networking in world.find_components(C.Networking):
      networking.spawn(id)

    #TODO: create player (this maybe should be a separate handler)
    world.create_entity([
      C.Networking(id),
      C.Position(Vector(2, 2)), #TODO: hardcoded position
      C.ServerPlayer(server)
    ])
    #tell the player he controls the newly spawned actor
    server.send(id, PlayerAssigned(id))

class ServerManager(Component):
  def __init__(self):
    super().__init__()
    self.queue = []
    self.server = None
    self.networked_entities = {}

  def network_register(self, entity):
    id = entity.get_component(C.Networking).id
    self.networked_entities[id] = entity
    #TODO: send spawned event (would require networking other components, not just actor)

  def network_unregister(self, entity):
    id = entity.get_component(C.Networking).id
    try:
      del self.networked_entities[id]
    except:
      print("[Server] ERROR: tried to delete entity that doesn't exist with id " + id)

  def start(self):
    #TODO: circular imports
    from game.networking.commands import PlayerMoveHandler, \
      PlayerUseSkillHandler, PlayerInteractHandler

    self.server = Server(
      connect_handlers=[ConnectHandler(self)],
      command_handlers=[
        PlayerMoveHandler(self),
        PlayerUseSkillHandler(self),
        PlayerInteractHandler(self),
      ],
    )
    self.server.start()
