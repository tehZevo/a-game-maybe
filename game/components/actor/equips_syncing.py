import game.networking.events as E

from game.ecs import Component
from game.components.networking.network_behavior import NetworkBehavior
from game.components.actor import EquipsListener
import game.components as C

class EquipsSyncing(Component, NetworkBehavior, EquipsListener):
  def __init__(self):
    super().__init__()
    self.require(C.Equips, C.Networking)
    self.equips = None
    
  def start(self):
    self.equips = self.entity[C.Equips]

  def make_event(self, equips, networking):
    armor = {k: v.id if v is not None else None for k, v in equips.armor.items()}
    skills = {k: v.id if v is not None else None for k, v in equips.skills.items()}
    weapons = {k: v.id if v is not None else None for k, v in equips.weapons.items()}
    return E.EquipsUpdated(
      id=networking.id,
      armor=armor,
      skills=skills,
      weapons=weapons,
    )

  def on_client_join(self, networking, client_id):
    event = self.make_event(self.equips, networking)
    print("B", event)
    networking.send_to_client(client_id, event)

  def on_equips_changed(self, equips):
    networking = self.get_component(C.Networking)
    if not networking.is_server:
      return

    event = self.make_event(equips, networking)
    networking.broadcast_synced(event)
