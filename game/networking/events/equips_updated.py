from dataclasses import dataclass

from game.utils import Vector
from ..event_handler import EventHandler
import game.components as C
from game.data.registry import get_item

@dataclass
class EquipsUpdated:
  id: str
  armor: dict
  skills: dict
  weapons: dict

class EquipsUpdatedHandler(EventHandler):
  def __init__(self):
    super().__init__(EquipsUpdated)

  def handle(self, client_manager, client, event):
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
