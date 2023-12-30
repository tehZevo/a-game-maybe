from game.ecs import Component
from game.networking import Client
from . import Id
# from game.networking.events import TilesetUpdatedHandler, ActorSpawnedHandler, \
from game.networking.events import TilesetUpdatedHandler, EntitySpawnedHandler, \
EntityDespawnedHandler, PositionUpdatedHandler, PlayerAssignedHandler, \
ItemSpawnedHandler, StatsUpdatedHandler

class ClientManager(Component):
  def __init__(self):
    super().__init__()
    self.networked_entities = {}

  def spawn(self, entity):
    id = entity.get_component(Id).id
    self.networked_entities[id] = entity

  def despawn(self, id):
    ent = self.networked_entities[id]
    del self.networked_entities[id]
    return ent

  def start(self):
    self.client = Client(
      event_handlers=[
        PlayerAssignedHandler(self),
        TilesetUpdatedHandler(self),
        # ActorSpawnedHandler(self),
        EntitySpawnedHandler(self),
        ItemSpawnedHandler(self),
        PositionUpdatedHandler(self),
        EntityDespawnedHandler(self),
        StatsUpdatedHandler(self),
      ]
    )
    self.client.connect()
