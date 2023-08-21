from game.networking.events import ActorSpawned
from . import Networking

class ActorNetworking(Networking):
  def __init__(self):
    super().__init__()
    #TODO: circular import
    from ..actor import Actor
    from . import PositionNetworking, DespawnNetworking, StatsNetworking
    self.require(Actor, PositionNetworking, DespawnNetworking, StatsNetworking)
    self.pos = None

  def start_server(self):
    #TODO: send SpriteChanged?
    #spawn actor on clients
    self.server_manager.server.broadcast(ActorSpawned(self.network_id))
