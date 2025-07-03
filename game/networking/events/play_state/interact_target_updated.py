from dataclasses import dataclass

from game.networking import PlayStateEventHandler
import game.components as C
from game.utils import Vector

#TODO: store item so client can display in ui?
@dataclass
class InteractTargetUpdated:
  pos: Vector | None

class InteractTargetUpdatedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(InteractTargetUpdated, game_state)

  def handle(self, event):
    world = self.game_state.world
    cursor = world.find_component(C.InteractCursor)
    if event.pos is not None and cursor is None:
      world.create_entity([
        C.Position(event.pos),
        C.InteractCursor()
      ])
    elif event.pos is None and cursor is not None:
      cursor.entity.remove()
    elif event.pos is not None and cursor is not None:
      cursor.entity[C.Position].pos = event.pos
