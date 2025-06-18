from game.ecs import Component
import game.components as C
from ..networking.network_behavior import NetworkBehavior

class ActorNetworking(Component, NetworkBehavior):
  def __init__(self):
    super().__init__()
    self.require(C.PositionSyncing, C.SpriteSyncing, C.StatsSyncing, \
      C.EquipsSyncing, C.BuffsSyncing)
