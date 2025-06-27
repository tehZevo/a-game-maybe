from dataclasses import dataclass

from game.networking import PlayStateEventHandler
import game.components as C
from game.data.registry import get_sprite
from game.utils import Vector

@dataclass
class ActionEnded:
  entity_id: str

class ActionEndedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(ActionEnded, game_state)

  def handle(self, event):
    #don't apply actions to player
    #TODO: may need to revisit if we impl stuns or "busy" as actions
    pc = self.game_state.world.find_component(C.PlayerController)
    if pc.id == event.entity_id:
      return
    client_manager = self.game_state.client_manager
    ent = client_manager.networked_entities.get(event.entity_id)
    if ent is None:
      return
    ent[C.Actor].action = None
