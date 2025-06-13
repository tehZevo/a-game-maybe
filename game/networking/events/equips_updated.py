from dataclasses import dataclass

from game.utils import Vector
from ..event_handler import EventHandler
import game.components as C

#TODO: how to network items themselves?
#TODO: we could network the ids
@dataclass
class EquipsUpdated:
  id: str
  armor: dict
  skills: dict
  weapons: dict
  cur_weapon: int

class EquipsUpdatedHandler(EventHandler):
  def __init__(self):
    super().__init__(EquipsUpdated)

  def handle(self, client_manager, client, event):
    if event.id not in client_manager.networked_entities:
      return

    #TODO: how to handle stats being recalculated from updating equips?
    #TODO: should we just calculate client side and send a hp/mp updated event?
    print("new equips:", event)
    ent = client_manager.networked_entities[event.id]
    equips = ent.get_component(C.Equips)
    equips.armor = event.armor
    equips.skills = event.skills
    equips.weapons = event.weapons
    equips.cur_weapon = event.cur_weapon
