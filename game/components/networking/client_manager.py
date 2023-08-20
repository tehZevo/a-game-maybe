from game.ecs import Component
from game.networking import Client
from game.networking.events import TilesetUpdatedHandler, ActorSpawnedHandler, \
  ActorDespawnedHandler, PositionUpdatedHandler, PlayerAssignedHandler
from . import Networked

class ClientManager(Component):
  def __init__(self):
    super().__init__()
    self.networked_entities = {}

  def spawn(self, entity):
    id = entity.get_component(Networked).id
    self.networked_entities[id] = entity

  def despawn(self, id):
    ent = self.networked_entities[id]
    del self.networked_entities[id]
    return ent

  def start(self):
    self.client = Client(
      event_handlers=[
        TilesetUpdatedHandler(self),
        ActorSpawnedHandler(self),
        ActorDespawnedHandler(self),
        PositionUpdatedHandler(self),
        PlayerAssignedHandler(self),
      ]
    )
    self.client.connect()
