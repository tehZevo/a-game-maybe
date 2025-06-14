from game.networking.events import EquipsUpdated

from game.ecs import Component
from game.components.networking.network_behavior import NetworkBehavior
from game.components.actor import EquipsListener
import game.components as C

class EquipsSyncing(Component, NetworkBehavior, EquipsListener):
  def __init__(self):
    super().__init__()
    self.require(C.Equips, C.Networking)

  def on_equips_changed(self, equips):
    networking = self.get_component(C.Networking)
    if not networking.is_server:
      return

    armor = {k: v.id if v is not None else None for k, v in equips.armor.items()}
    skills = {k: v.id if v is not None else None for k, v in equips.skills.items()}
    weapons = {k: v.id if v is not None else None for k, v in equips.weapons.items()}
    evt = EquipsUpdated(
      id=networking.id,
      armor=armor,
      skills=skills,
      weapons=weapons,
    )
    networking.broadcast_synced(evt)
