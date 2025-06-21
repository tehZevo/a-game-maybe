from dataclasses import dataclass

from ..command_handler import CommandHandler
from game.utils import Vector
import game.components as C
import game.networking.events as E
from game.constants import REPORT_POS_ERROR_THRESH

@dataclass
class ReportPosition:
  id: str
  pos: Vector

class ReportPositionHandler(CommandHandler):
  def __init__(self):
    super().__init__(ReportPosition)

  def handle(self, server_manager, server, client_id, command):
    ent = server_manager.networked_entities.get(command.id)
    if ent is None:
      return
    pos_comp = ent[C.Position]
    if command.pos.distance(pos_comp.pos) > REPORT_POS_ERROR_THRESH:
      server.send(client_id, E.PositionUpdated(command.id, pos_comp.pos))
