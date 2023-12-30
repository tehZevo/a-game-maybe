from game.utils import Vector

from game.components.networking.networking import Networking

class Position(Networking):
  def __init__(self, pos=None):
    super().__init__()
    self.pos = Vector() if pos is None else pos

  def update_server(self):
    #TODO: circular import
    from game.networking.events import PositionUpdated
    self.server_manager.server.broadcast(PositionUpdated(self.network_id, self.pos))
