from game.networking.events import EntityDespawned
from . import Networking

class DespawnNetworking(Networking):
  def __init__(self):
    super().__init__()

  def on_destroy_server(self):
    self.server_manager.despawn(self.entity)
    self.server_manager.server.broadcast(EntityDespawned(self.network_id))
