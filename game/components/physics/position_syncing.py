from game.ecs import Component
from game.utils import Vector
import game.components as C
from game.components.networking import Networking

class PositionSyncing(Component, Networking):
  def __init__(self, pos=None):
    super().__init__()

  def start_server(self):
    self.pos = self.get_component(C.Position)

  def update_server(self):
    #TODO: circular import
    from game.networking.events import PositionUpdated
    #TODO: pass this in instead...
    networked = self.get_component(C.Networked)
    networked.server_manager.server.broadcast(PositionUpdated(networked.id, self.pos.pos))
