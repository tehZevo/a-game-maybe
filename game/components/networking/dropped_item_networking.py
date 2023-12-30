from game.networking.events import ItemSpawned
import game.components as C
from . import Networking

class DroppedItemNetworking(Networking):
  def __init__(self):
    super().__init__()
    self.require(C.DroppedItem)

  def start_server(self):
    self.server_manager.server.broadcast(ItemSpawned(self.network_id, self.get_component(C.DroppedItem).item.__class__.__name__))
