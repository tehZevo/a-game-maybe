from dataclasses import dataclass

from game.utils import Vector
from ..event_handler import EventHandler
import game.components as C
from game.data.registry import get_mob

#TODO: split into MobMovePosUpdated and MobDefUpdated?
@dataclass
class MobUpdated:
  id: str
  mobdef: str
  move_pos: Vector | None

class MobUpdatedHandler(EventHandler):
  def __init__(self):
    super().__init__(MobUpdated)

  def handle(self, client_manager, client, event):
    ent = client_manager.networked_entities.get(event.id)
    if ent is None:
      return

    ent[C.Enemy].mobdef = get_mob(event.mobdef)
    ent[C.Enemy].move_pos = event.move_pos
