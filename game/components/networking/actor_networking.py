# from game.networking.events import ActorSpawned
from game.networking.events import EntitySpawned
from .networking import Networking
from .networkable import Networkable
from .networked import Networked

class ActorNetworking(Networking):
  def __init__(self):
    super().__init__()
    #TODO: circular import
    from ..actor import Actor
    from . import PositionNetworking, DespawnNetworking, StatsNetworking
    self.require(Actor, PositionNetworking, DespawnNetworking, StatsNetworking, Networked)
    self.pos = None

  # def start_server(self):
  #   #TODO: send SpriteChanged?
  #   #spawn actor on clients
  #   spawn_data = {k: v.melt() for k, v in self.entity.components.items() if isinstance(v, Networkable)}
  #   self.server_manager.server.broadcast(EntitySpawned(self.network_id, {
  #     **spawn_data,
  #     "Actor": {}
  #   }))
