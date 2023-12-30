from game.ecs import Component
from game.networking import Client
from game.networking.events import TilesetUpdatedHandler, EntitySpawnedHandler, \
EntityDespawnedHandler, PositionUpdatedHandler, PlayerAssignedHandler, \
ItemSpawnedHandler, StatsUpdatedHandler, SpriteChangedHandler
import game.components as C

class ClientManager(Component):
  def __init__(self):
    super().__init__()
    self.networked_entities = {}

  def network_register(self, entity):
    id = entity.get_component(C.Networking).id
    self.networked_entities[id] = entity

  def network_unregister(self, id):
    ent = self.networked_entities[id]
    del self.networked_entities[id]
    return ent

  def start(self):
    self.client = Client(
      event_handlers=[
        PlayerAssignedHandler(self),
        TilesetUpdatedHandler(self),
        EntitySpawnedHandler(self),
        ItemSpawnedHandler(self),
        PositionUpdatedHandler(self),
        SpriteChangedHandler(self),
        EntityDespawnedHandler(self),
        StatsUpdatedHandler(self),
      ]
    )
    self.client.connect()
