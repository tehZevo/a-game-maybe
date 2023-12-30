from game.networking.events import StatsUpdated

from game.ecs import Component
from game.components.networking import Networking

#TODO: solve circular dependencies by implementing equiplistener?
class Stats(Networking):
  def __init__(self):
    super().__init__()
    #TODO: calculate
    self.hp = 1
    self.mp = 1
    self.move_speed_multiplier = 1
    self.primary_stats = self.equip_stats = self.secondary_stats = None

  def start(self):
    super().start()
    self.recalculate()
    self.hp = self.secondary_stats.hp
    self.mp = self.secondary_stats.mp

  def stats_changed(self):
    self.alert_listeners()

    if self.is_server:
      self.server_manager.server.broadcast(StatsUpdated(
        id=self.network_id,
        primary_stats=self.primary_stats,
        secondary_stats=self.secondary_stats,
        equip_stats=self.equip_stats,
        hp=self.hp,
        mp=self.mp,
        move_speed_multiplier=self.move_speed_multiplier,
      ))

  def alert_listeners(self):
    #TODO: circular import
    from . import StatsListener
    #TODO: a single skill use generates a LOT of stats updated events lol
    #- maybe add separate events for (current) hp/mp updated
    for listener in self.entity.find(StatsListener):
      listener.on_stats_changed(self)

  def add_hp(self, hp):
    self.set_hp(self.hp + hp)
    self.stats_changed()

  def add_mp(self, mp):
    self.set_mp(self.mp + mp)
    self.stats_changed()

  def set_hp(self, hp):
    self.hp = int(max(0, min(hp, self.secondary_stats.hp)))
    self.stats_changed()

  def set_mp(self, mp):
    self.mp = int(max(0, min(mp, self.secondary_stats.mp)))
    self.stats_changed()

  def recalculate(self):
    #TODO: circlular import
    from game.stats import calculator
    self.primary_stats, self.equip_stats, self.secondary_stats = calculator.calculate(self.entity)
    self.hp = min(self.hp, self.secondary_stats.hp)
    self.mp = min(self.mp, self.secondary_stats.mp)
    self.stats_changed()
