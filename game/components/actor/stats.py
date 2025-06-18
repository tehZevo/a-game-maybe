from game.ecs import Component
import game.components as C

#TODO: where should hp/mp live?
class Stats(Component):
  def __init__(self):
    super().__init__()
    #TODO: calculate
    #because recalculate (calculate) requires armor, etc, we technically depend on a full actor
    #but it would be better for actor to have the calculate logic i think idk
    self.require(C.Actor)
    self.hp = 1
    self.mp = 1
    #TODO: dont store this here... (actor or just use stat modifiers?)
    self.move_speed_multiplier = 1
    self.stats = None #TODO: rename calculated?
    self.flat_modifiers = {}
    self.scaling_modifiers = {}

  def start(self):
    super().start()
    self.recalculate()
    self.hp = self.stats.secondary.hp
    self.mp = self.stats.secondary.mp

  def add_flat_modifier(self, id, modifier):
    self.flat_modifiers[id] = modifier
    self.recalculate()
  
  def add_scaling_modifier(self, id, modifier):
    self.scaling_modifiers[id] = modifier
    self.recalculate()
  
  def remove_flat_modifier(self, id):
    del self.flat_modifiers[id]
    self.recalculate()
  
  def remove_scaling_modifier(self, id):
    del self.scaling_modifiers[id]
    self.recalculate()

  def alert_listeners(self):
    #TODO: a single skill use generates a LOT of stats updated events lol
    #- maybe add separate events for (current) hp/mp updated
    #TODO: use dirty flag (causes 1 tick delay)
    #TODO: also only send update if stats are not the same.. (can use dataclass equality i think)
    for listener in self.entity.find(C.StatsListener):
      listener.on_stats_changed(self)

  def add_hp(self, hp):
    self.set_hp(self.hp + hp)
    self.alert_listeners()
  
  def add_hp_percent(self, percent):
    self.add_hp(self.stats.secondary.hp * percent)

  def add_mp(self, mp):
    self.set_mp(self.mp + mp)
    self.alert_listeners()

  def add_mp_percent(self, percent):
    self.add_mp(self.stats.secondary.mp * percent)

  def set_hp(self, hp):
    self.hp = int(max(0, min(hp, self.stats.secondary.hp)))
    self.alert_listeners()

  def set_mp(self, mp):
    self.mp = int(max(0, min(mp, self.stats.secondary.mp)))
    self.alert_listeners()

  def recalculate(self):
    from game.stats import calculator
    #TODO: get additions from buffs
    self.stats = calculator.calculate(self.entity)
    self.hp = min(self.hp, self.stats.secondary.hp)
    self.mp = min(self.mp, self.stats.secondary.mp)
    self.alert_listeners()
