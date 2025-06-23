from dataclasses import dataclass

from game.networking import PlayStateCommandHandler
from game.utils import Vector
import game.components as C
import game.networking.events as E
from game.constants import REPORT_POS_ERROR_THRESH

@dataclass
class ReportPosition:
  id: str
  pos: Vector

class ReportPositionHandler(PlayStateCommandHandler):
  def __init__(self, game_state):
    super().__init__(ReportPosition, game_state)

  def handle(self, client_id, command):
    server_manager = self.game_state.server_manager
    ent = server_manager.networked_entities.get(command.id)
    if ent is None:
      return
    pos_comp = ent[C.Position]
    if command.pos.distance(pos_comp.pos) > REPORT_POS_ERROR_THRESH:
      server.send(client_id, E.PositionUpdated(command.id, pos_comp.pos))
