from dataclasses import dataclass

from game.utils import Vector
from game.networking import PlayStateEventHandler
import game.components as C
from game.data.registry import get_mob

#TODO: split into MobMovePosUpdated and MobDefUpdated?
@dataclass
class MobUpdated:
  id: str
  mobdef: str
  move_pos: Vector | None

class MobUpdatedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(MobUpdated, game_state)

  def handle(self, event):
    client_manager = self.game_state.client_manager
    ent = client_manager.networked_entities.get(event.id)
    if ent is None:
      return

    ent[C.Enemy].mobdef = get_mob(event.mobdef)
    ent[C.Enemy].move_pos = event.move_pos
