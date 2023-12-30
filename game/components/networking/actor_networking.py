from game.networking.events import EntitySpawned
import game.components as C
from .networking import Networking

class ActorNetworking(Networking):
  def __init__(self):
    super().__init__()
    self.require(C.Actor, C.Networked)
