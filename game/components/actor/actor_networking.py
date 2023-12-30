from game.ecs import Component
import game.components as C
from ..networking.networking import Networking

class ActorNetworking(Component, Networking):
  def __init__(self):
    super().__init__()
    self.require(C.PositionSyncing, C.SpriteSyncing, C.StatsSyncing)
