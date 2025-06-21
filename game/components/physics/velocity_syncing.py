from game.ecs import Component
from game.utils import Vector
import game.components as C
from game.components.networking.network_behavior import NetworkBehavior
from game.constants import DT, PHYS_REPORT_RATE
import game.networking.events as E
import game.networking.commands as Commands

class VelocitySyncing(Component, NetworkBehavior):
  def __init__(self, pos=None):
    super().__init__()
    self.require(C.Physics, C.Networking)
    self.last_client_report_time = float("inf")

  def on_client_join(self, networking, client_id):
    event = E.VelocityUpdated(networking.id, self.entity[C.Physics].vel)
    networking.send_to_client(client_id, event)

  def update_client(self, networking):
    self.last_client_report_time += DT
    if self.last_client_report_time >= PHYS_REPORT_RATE:
      self.last_client_report_time = 0
      #TODO: fix networking id being none here (dropped item)
      if networking.id is None:
        return
      networking.send_to_server(Commands.ReportVelocity(networking.id, self.entity[C.Physics].vel))
