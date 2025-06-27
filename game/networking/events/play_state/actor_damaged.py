from dataclasses import dataclass

from game.networking import PlayStateEventHandler
import game.components as C
from game.data.registry import get_sprite
from game.utils import Vector
from game.actions import Action

@dataclass
class ActorDamaged:
  entity_id: str
  amount: int

class ActorDamagedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(ActorDamaged, game_state)

  def handle(self, event):
    client_manager = self.game_state.client_manager
    ent = client_manager.networked_entities.get(event.entity_id)
    if ent is None:
      return
    pos = ent[C.Position].pos.copy()
    ent.world.create_entity([
      C.Position(pos),
      C.DamageNumber(event.amount)
    ])
