from game.ecs import Component
import game.components as C
from game.components.networking.network_behavior import NetworkBehavior

class StairsNetworking(Component, NetworkBehavior):
  def __init__(self):
    super().__init__()
    #NOTE: doesnt actually spawn stairs component because that requires a generator, which client doesnt have access to...
    self.require(C.SpriteSyncing, C.PositionSyncing)
