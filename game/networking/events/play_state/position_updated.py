from dataclasses import dataclass

from game.utils import Vector
from game.networking import PlayStateEventHandler
import game.components as C

@dataclass
class PositionUpdated:
  id: str
  pos: Vector

class PositionUpdatedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(PositionUpdated, game_state)

  def handle(self, event):
    client_manager = self.game_state.client_manager
    ent = client_manager.networked_entities.get(event.id)
    if ent is None:
      return
    ent = client_manager.networked_entities[event.id]
    if ent is not None:
      ent[C.Position].pos = event.pos
      ent[C.PositionSyncing].last_pos = event.pos
