from dataclasses import dataclass

from ..command_handler import CommandHandler
from game.utils import Vector
import game.components as C
import game.networking.events as E
from game.utils.constants import REPORT_VEL_ERROR_THRESH

@dataclass
class ReportVelocity:
  id: str
  vel: Vector

class ReportVelocityHandler(CommandHandler):
  def __init__(self):
    super().__init__(ReportVelocity)

  def handle(self, server_manager, server, client_id, command):
    ent = server_manager.networked_entities.get(command.id)
    if ent is None:
      return
    phys_comp = ent[C.Physics]
    if command.vel.distance(phys_comp.vel) > REPORT_VEL_ERROR_THRESH:
      server.send(client_id, E.VelocityUpdated(command.id, phys_comp.vel))
