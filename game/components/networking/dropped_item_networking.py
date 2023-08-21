from game.networking.events import ItemSpawned, EntityDespawned, PositionUpdated
from ..physics import Position
from . import Networking

class DroppedItemNetworking(Networking):
  def __init__(self):
    super().__init__()
    #TODO: circular import
    from ..item import DroppedItem
    self.require(DroppedItem)
    self.pos = None

  def start_server(self):
    #TODO: circular import
    from ..item import DroppedItem
    self.pos = self.get_component(Position)
    #TODO: send SpriteChanged?
    #spawn actor on clients
    self.server_manager.server.broadcast(ItemSpawned(self.network_id, self.get_component(DroppedItem).item.__class__.__name__))

  def update_server(self):
    #TODO: move to some kind of position/physics sync
    self.server_manager.server.broadcast(PositionUpdated(self.network_id, self.pos.pos))

  def on_destroy_server(self):
    self.server_manager.server.broadcast(EntityDespawned(self.network_id))
