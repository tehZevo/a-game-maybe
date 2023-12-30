from game.ecs import Component
import game.components as C
from game.components.networking.network_behavior import NetworkBehavior

class ChestNetworking(Component, NetworkBehavior):
  def __init__(self):
    super().__init__()
    self.require(C.SpriteSyncing, C.PositionSyncing)
