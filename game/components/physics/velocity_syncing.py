from game.ecs import Component
from game.utils import Vector
import game.components as C
from game.components.networking.network_behavior import NetworkBehavior
from game.utils.constants import NETWORK_VEL_MAX_DIST
import game.networking.events as E

class VelocitySyncing(Component, NetworkBehavior):
  def __init__(self, pos=None):
    super().__init__()
    self.require(C.Physics)
    self.last_vel = None

  def start_server(self, networking):
    self.phys_comp = self.get_component(C.Physics)
    self.last_vel = self.phys_comp.vel.copy()
  
  def on_client_join(self, networking, client_id):
    networking = self.get_component(C.Networking)
    event = E.VelocityUpdated(networking.id, self.phys_comp.vel)
    networking.send_to_client(client_id, event)

  def update_server(self, networking):
    new_vel = self.phys_comp.vel.copy()
    if self.last_vel.distance(new_vel) > NETWORK_VEL_MAX_DIST:
      event = E.VelocityUpdated(networking.id, new_vel)
      networking.broadcast_synced(event)
      self.last_vel = new_vel
