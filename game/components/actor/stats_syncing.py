from game.networking.events import StatsUpdated

from game.ecs import Component
from game.components.networking.networking import Networking
from game.components.actor import StatsListener
import game.components as C

class StatsSyncing(Component, Networking, StatsListener):
  def __init__(self):
    super().__init__()
    self.require(C.Stats, C.Networked)

  def on_stats_changed(self, stats):
    #TODO: networked seems like a weird name here
    networked = self.get_component(C.Networked)
    if networked.is_server:
      networked.server_manager.server.broadcast(StatsUpdated(
        id=networked.id,
        primary_stats=stats.primary_stats,
        secondary_stats=stats.secondary_stats,
        equip_stats=stats.equip_stats,
        hp=stats.hp,
        mp=stats.mp,
        move_speed_multiplier=stats.move_speed_multiplier,
      ))
