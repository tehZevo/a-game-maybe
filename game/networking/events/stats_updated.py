from dataclasses import dataclass

from game.utils import Vector
from ..event_handler import EventHandler
from game.components.actor import Stats
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
  def __init__(self, client_manager):
    super().__init__(StatsUpdated)
    self.client_manager = client_manager

  def handle(self, client, event):
    if event.id not in self.client_manager.networked_entities:
      return

    ent = self.client_manager.networked_entities[event.id]
    stats = ent.get_component(Stats)
    stats.hp = event.hp
    stats.mp = event.mp
    stats.move_speed_multiplier = event.move_speed_multiplier
    stats.primary_stats = event.primary_stats
    #TODO: maybe we should call recalculate instead of sending secondary stats over the wire?
    stats.secondary_stats = event.secondary_stats
    stats.equip_stats = event.equip_stats
    #TODO: recalculate?
    # stats.recalculate()
