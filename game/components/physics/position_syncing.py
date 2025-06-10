from game.ecs import Component
from game.utils import Vector
import game.components as C
from game.components.networking.network_behavior import NetworkBehavior

class PositionSyncing(Component, NetworkBehavior):
  def __init__(self, pos=None):
    super().__init__()

  def start_server(self, networking):
    self.pos = self.get_component(C.Position)
  
  def on_client_join(self, networking, client_id):
    #TODO: circular import
    from game.networking.events import PositionUpdated
    networking = self.get_component(C.Networking)
    networking.send_to_client(client_id, PositionUpdated(networking.id, self.pos.pos))

  def update_server(self, networking):
    #TODO: only send move if distance above a threshold
    #TODO: circular import
    from game.networking.events import PositionUpdated
    networking.broadcast(PositionUpdated(networking.id, self.pos.pos))
