from game.ecs import Component
from . import StatsListener

#TODO: solve circular dependencies by implementing equiplistener?
class Stats(Component):
  def __init__(self):
    super().__init__()
    #TODO: calculate
    self.hp = 1
    self.mp = 1
    self.move_speed_multiplier = 1
    self.primary_stats = self.equip_stats = self.secondary_stats = None

  def start(self):
    self.recalculate()
    self.hp = self.secondary_stats.hp
    self.mp = self.secondary_stats.mp

  def alert_listeners(self):
    #TODO: a single skill use generates a LOT of stats updated events lol
    #- maybe add separate events for (current) hp/mp updated
    for listener in self.entity.find(StatsListener):
      listener.on_stats_changed(self)

  def add_hp(self, hp):
    self.set_hp(self.hp + hp)
    self.alert_listeners()

  def add_mp(self, mp):
    self.set_mp(self.mp + mp)
    self.alert_listeners()

  def set_hp(self, hp):
    self.hp = int(max(0, min(hp, self.secondary_stats.hp)))
    self.alert_listeners()

  def set_mp(self, mp):
    self.mp = int(max(0, min(mp, self.secondary_stats.mp)))
    self.alert_listeners()

  def recalculate(self):
    #TODO: circlular import
    from game.stats import calculator
    self.primary_stats, self.equip_stats, self.secondary_stats = calculator.calculate(self.entity)
    self.hp = min(self.hp, self.secondary_stats.hp)
    self.mp = min(self.mp, self.secondary_stats.mp)
    self.alert_listeners()
