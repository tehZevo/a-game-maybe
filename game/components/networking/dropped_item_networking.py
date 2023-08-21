from game.networking.events import ItemSpawned
from . import Networking, PositionNetworking, DespawnNetworking

class DroppedItemNetworking(Networking):
  def __init__(self):
    super().__init__()
    #TODO: circular import
    from ..item import DroppedItem
    self.require(DroppedItem, PositionNetworking, DespawnNetworking)
    self.pos = None

  def start_server(self):
    #TODO: circular import
    from ..item import DroppedItem
    self.server_manager.server.broadcast(ItemSpawned(self.network_id, self.get_component(DroppedItem).item.__class__.__name__))
