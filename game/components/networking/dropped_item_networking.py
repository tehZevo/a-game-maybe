from game.networking.events import ItemSpawned
import game.components as C
from . import Networking

class DroppedItemNetworking(Networking):
  def __init__(self):
    super().__init__()
    self.require(C.DroppedItem, C.PositionNetworking, C.DespawnNetworking)
    self.pos = None

  def start_server(self):
    #TODO: circular import
    from ..item import DroppedItem
    self.server_manager.server.broadcast(ItemSpawned(self.network_id, self.get_component(DroppedItem).item.__class__.__name__))
