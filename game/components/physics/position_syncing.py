from game.ecs import Component
from game.utils import Vector
import game.components as C
from game.components.networking.network_behavior import NetworkBehavior

class PositionSyncing(Component, NetworkBehavior):
  def __init__(self, pos=None):
    super().__init__()

  def start_server(self, networking):
    self.pos = self.get_component(C.Position)

  def update_server(self, networking):
    #TODO: circular import
    from game.networking.events import PositionUpdated
    networking.server_manager.server.broadcast(PositionUpdated(networking.id, self.pos.pos))
