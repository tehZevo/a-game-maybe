from game.ecs import Component
from game.networking import Client
from game.networking.events import TilesetUpdatedHandler, ActorSpawnedHandler, \
  PositionUpdatedHandler, PlayerAssignedHandler

class ClientManager(Component):
  def __init__(self):
    super().__init__()

  def start(self):
    self.client = Client(
      event_handlers=[
        TilesetUpdatedHandler(self),
        ActorSpawnedHandler(self),
        PositionUpdatedHandler(self),
        PlayerAssignedHandler(self),
      ]
    )
    self.client.connect()
