from dataclasses import dataclass

from game.utils import Vector
from game.networking import PlayStateEventHandler
import game.components as C
from game.stats import Stats, PrimaryStats, SecondaryStats, EquipStats

#TODO: use full Stats class instead
@dataclass
class StatsUpdated:
  id: str
  primary_stats: PrimaryStats
  secondary_stats: SecondaryStats
  equip_stats: EquipStats
  hp: int
  mp: int
  move_speed_multiplier: float

class StatsUpdatedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(StatsUpdated, game_state)

  def handle(self, event):
    client_manager = self.game_state.client_manager
    if event.id not in client_manager.networked_entities:
      return

    ent = client_manager.networked_entities[event.id]
    stats = ent[C.Stats]
    stats.hp = event.hp
    stats.mp = event.mp
    stats.move_speed_multiplier = event.move_speed_multiplier
    stats.stats = Stats(
      equip=event.equip_stats,
      primary=event.primary_stats,
      secondary=event.secondary_stats
    )
