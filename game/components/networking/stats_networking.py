from game.networking.events import StatsUpdated
from ..actor import StatsListener
from . import Networking

#sends StatsUpdated events
class StatsNetworking(Networking, StatsListener):
  def __init__(self):
    super().__init__()

  def on_stats_changed(self, stats):
    if not self.is_server:
      return

    self.server_manager.server.broadcast(StatsUpdated(
      id=self.network_id,
      primary_stats=stats.primary_stats,
      secondary_stats=stats.secondary_stats,
      equip_stats=stats.equip_stats,
      hp=stats.hp,
      mp=stats.mp,
      move_speed_multiplier=stats.move_speed_multiplier,
    ))
