from game.networking.events import EntitySpawned

from .networkable import Networkable
from .networking import Networking

class Networked(Networking):
  def __init__(self):
    super().__init__()

  #spawn entity on start
  def start_server(self):
    self.server_manager.server.broadcast(EntitySpawned(self.network_id, self.get_spawn_data()))

  def get_spawn_data(self):
    spawn_data = {k: v.melt() for k, v in self.entity.components.items() if isinstance(v, Networkable)}
    return spawn_data
