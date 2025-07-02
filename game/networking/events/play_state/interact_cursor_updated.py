from dataclasses import dataclass

from game.networking import PlayStateEventHandler
import game.components as C
from game.utils import Vector

#TODO: store item so client can display in ui?
#TODO: where to store resulting pos?
@dataclass
class InteractCursorUpdated:
  pos: Vector

class InteractCursorUpdatedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(InteractCursorUpdated, game_state)

  def handle(self, e):
    #TODO
    pass
