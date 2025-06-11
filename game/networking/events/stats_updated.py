from dataclasses import dataclass

from game.utils import Vector
from ..event_handler import EventHandler
import game.components as C
from game.stats import PrimaryStats, SecondaryStats, EquipStats

#TODO: maybe need a FullStats dataclass that stores all this data
@dataclass
class StatsUpdated:
  id: str
  primary_stats: PrimaryStats
  secondary_stats: SecondaryStats
  equip_stats: EquipStats
  hp: int
  mp: int
  move_speed_multiplier: float

class StatsUpdatedHandler(EventHandler):
  def __init__(self):
    super().__init__(StatsUpdated)

  def handle(self, client_manager, client, event):
    if event.id not in client_manager.networked_entities:
      return

    ent = client_manager.networked_entities[event.id]
    stats = ent.get_component(C.Stats)
    stats.hp = event.hp
    stats.mp = event.mp
    stats.move_speed_multiplier = event.move_speed_multiplier
    stats.primary_stats = event.primary_stats
    #TODO: maybe we should call recalculate instead of sending secondary stats over the wire?
    stats.secondary_stats = event.secondary_stats
    stats.equip_stats = event.equip_stats
    #TODO: recalculate?
    # stats.recalculate()
