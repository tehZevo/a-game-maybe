from dataclasses import dataclass

from game.networking import PlayStateEventHandler
import game.components as C
from game.data.registry import get_item

@dataclass
class EquipsUpdated:
  id: str
  armor: dict
  skills: dict
  weapons: dict

class EquipsUpdatedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(EquipsUpdated, game_state)

  def handle(self, event):
    client_manager = self.game_state.client_manager
    if event.id not in client_manager.networked_entities:
      return

    #TODO: avoid calculating stats on client and just wait for stats updated
    #hydrate equips
    armor = {int(k): get_item(v) if v is not None else None for k, v in event.armor.items()}
    skills = {int(k): get_item(v) if v is not None else None for k, v in event.skills.items()}
    weapons = {int(k): get_item(v) if v is not None else None for k, v in event.weapons.items()}
    #TODO: create equips function that sets all 3 and then recalculates
    ent = client_manager.networked_entities[event.id]
    equips = ent.get_component(C.Equips)
    equips.armor = armor
    equips.skills = skills
    equips.weapons = weapons
