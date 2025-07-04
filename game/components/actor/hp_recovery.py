from game.ecs import Component
import game.components as C
from game.components.networking import NetworkBehavior
from game.constants import HP_RECOVERY_PERCENT, HP_RECOVERY_TIME, DT

class HPRecovery(Component, NetworkBehavior):
  def __init__(self):
    super().__init__()
    self.require(C.Stats)
    self.always_recover = False
    self.time_since_last_recovery = 0

  def update_server(self, networking):
    actor = self.entity[C.Actor]
    self.time_since_last_recovery += DT
    
    if actor.in_combat and not self.always_recover:
      return
    
    if self.time_since_last_recovery > HP_RECOVERY_TIME:
      self.time_since_last_recovery = 0
      max_hp = self.entity[C.Stats].stats.secondary.hp
      actor.heal(max_hp * HP_RECOVERY_PERCENT / 100)