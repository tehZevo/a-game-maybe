from dataclasses import dataclass

from game.networking import PlayStateCommandHandler
from game.utils import Vector
import game.components as C
import game.networking.events as E
from game.constants import REPORT_VEL_ERROR_THRESH

@dataclass
class ReportVelocity:
  id: str
  vel: Vector

class ReportVelocityHandler(PlayStateCommandHandler):
  def __init__(self, game_state):
    super().__init__(ReportVelocity, game_state)

  def handle(self, client_id, command):
    server_manager = self.game_state.server_manager
    server = server_manager.server
    ent = server_manager.networked_entities.get(command.id)
    if ent is None:
      return
    phys_comp = ent[C.Physics]
    if command.vel.distance(phys_comp.vel) > REPORT_VEL_ERROR_THRESH:
      server.send(client_id, E.VelocityUpdated(command.id, phys_comp.vel))
