import game.networking.events as E

from game.ecs import Component
from game.components.networking.network_behavior import NetworkBehavior
from game.components.actor import StatsListener
import game.components as C

class StatsSyncing(Component, NetworkBehavior, StatsListener):
  def __init__(self):
    super().__init__()
    self.require(C.Stats, C.Networking)

  def on_stats_changed(self, stats):
    networking = self.get_component(C.Networking)
    if networking.is_server:
      evt = E.StatsUpdated(
        id=networking.id,
        primary_stats=stats.stats.primary,
        secondary_stats=stats.stats.secondary,
        equip_stats=stats.stats.equip,
        hp=stats.hp,
        mp=stats.mp,
        move_speed_multiplier=stats.move_speed_multiplier,
      )
      networking.broadcast_synced(evt)
