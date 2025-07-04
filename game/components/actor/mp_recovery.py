from game.ecs import Component
import game.components as C
from game.components.networking import NetworkBehavior
from game.constants import MP_RECOVERY_PERCENT, MP_RECOVERY_TIME, DT

class MPRecovery(Component, NetworkBehavior):
  def __init__(self):
    super().__init__()
    self.require(C.Stats)
    self.time_since_last_recovery = 0

  def update_server(self, networking):
    actor = self.entity[C.Actor]
    self.time_since_last_recovery += DT
    
    if self.time_since_last_recovery > MP_RECOVERY_TIME:
      self.time_since_last_recovery = 0
      max_mp = self.entity[C.Stats].stats.secondary.mp
      actor.heal_mp(max_mp * MP_RECOVERY_PERCENT / 100)