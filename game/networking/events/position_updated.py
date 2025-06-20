from dataclasses import dataclass

from game.utils import Vector
from ..event_handler import EventHandler
import game.components as C

@dataclass
class PositionUpdated:
  id: str
  pos: Vector

class PositionUpdatedHandler(EventHandler):
  def __init__(self):
    super().__init__(PositionUpdated)

  def handle(self, client_manager, client, event):
    ent = client_manager.networked_entities.get(event.id)
    if ent is None:
      return
    ent = client_manager.networked_entities[event.id]
    if ent is not None:
      ent[C.Position].pos = event.pos
      ent[C.PositionSyncing].last_pos = event.pos
