from game.networking.events import PositionUpdated
import game.components as C
from . import Networking

#just sends position updated to clients
class PositionNetworking(Networking):
  def __init__(self):
    super().__init__()
    self.require(C.Position)
    self.pos = None

  def start_server(self):
    self.pos = self.get_component(C.Position)

  def update_server(self):
    self.server_manager.server.broadcast(PositionUpdated(self.network_id, self.pos.pos))
