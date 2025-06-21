from game.ecs import Component
from game.utils import Vector
import game.components as C
from game.components.networking.network_behavior import NetworkBehavior
from game.constants import DT, PHYS_REPORT_RATE
import game.networking.events as E
import game.networking.commands as Commands

class PositionSyncing(Component, NetworkBehavior):
  def __init__(self, pos=None):
    super().__init__()
    self.require(C.Position, C.Networking)
    self.last_client_report_time = float("inf")

  def make_event(self, networking):
    return E.PositionUpdated(networking.id, self.entity[C.Position].pos)
    
  def on_client_join(self, networking, client_id):
    networking.send_to_client(client_id, self.make_event(networking))
  
  def start_server(self, networking):
    networking.broadcast_synced(self.make_event(networking))
  
  def update_client(self, networking):
    self.last_client_report_time += DT
    if self.last_client_report_time >= PHYS_REPORT_RATE:
      self.last_client_report_time = 0
      #TODO: fix networking.id being none here (dropped item)
      if networking.id is None:
        return
      command = Commands.ReportPosition(networking.id, self.entity[C.Position].pos)
      networking.send_to_server(command)
