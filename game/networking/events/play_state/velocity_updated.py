from dataclasses import dataclass

from game.utils import Vector
from game.networking import PlayStateEventHandler
import game.components as C

@dataclass
class VelocityUpdated:
  id: str
  vel: Vector

class VelocityUpdatedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(VelocityUpdated, game_state)

  def handle(self, event):
    client_manager = self.game_state.client_manager
    if event.id not in client_manager.networked_entities:
      return
    ent = client_manager.networked_entities[event.id]
    ent.get_component(C.Physics).vel = event.vel
