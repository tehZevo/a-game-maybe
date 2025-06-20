from game.ecs import Component
from game.utils import Vector
import game.components as C
from game.components.networking.network_behavior import NetworkBehavior
from game.utils.constants import NETWORK_POS_MAX_DIST, DT, PHYS_REPORT_RATE
import game.networking.events as E
import game.networking.commands as Commands

class PositionSyncing(Component, NetworkBehavior):
  def __init__(self, pos=None):
    super().__init__()
    self.require(C.Position)
    self.last_pos = None
    self.last_report_time = 0

  def start_client(self, networking):
    self.pos_comp = self.get_component(C.Position)
    
  def start_server(self, networking):
    self.pos_comp = self.get_component(C.Position)
    self.last_pos = self.pos_comp.pos.copy()
  
  def on_client_join(self, networking, client_id):
    networking = self.get_component(C.Networking)
    networking.send_to_client(client_id, E.PositionUpdated(networking.id, self.pos_comp.pos))

  def update_client(self, networking):
    self.last_report_time += DT
    if self.last_report_time >= PHYS_REPORT_RATE:
      self.last_report_time = 0
      networking.send_to_server(Commands.ReportPosition(networking.id, self.pos_comp.pos))
  
  def update_server(self, networking):
    new_pos = self.pos_comp.pos.copy()
    if self.last_pos.distance(new_pos) > NETWORK_POS_MAX_DIST:
      networking.broadcast_synced(E.PositionUpdated(networking.id, new_pos))
      self.last_pos = new_pos
