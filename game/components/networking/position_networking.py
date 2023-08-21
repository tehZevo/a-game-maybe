from game.networking.events import PositionUpdated
from ..physics import Position
from . import Networking

#just sends position updated to clients
class PositionNetworking(Networking):
  def __init__(self):
    super().__init__()
    self.require(Position)
    self.pos = None

  def start_server(self):
    self.pos = self.get_component(Position)

  def update_server(self):
    self.server_manager.server.broadcast(PositionUpdated(self.network_id, self.pos.pos))