from game.networking.events import ActorSpawned, EntityDespawned, PositionUpdated
from ..physics import Position
from . import Networking

#TODO: may need to make this more general (eg for tile entities)
#determine if we are on the client or the server
class ActorNetworking(Networking):
  def __init__(self):
    super().__init__()
    #TODO: circular import
    from ..actor import Actor
    self.require(Actor)
    self.pos = None

  def start_server(self):
    self.pos = self.get_component(Position)
    #TODO: send SpriteChanged?
    #spawn actor on clients
    self.server_manager.server.broadcast(ActorSpawned(self.network_id))

  def update_server(self):
    #TODO: move to some kind of position/physics sync
    self.server_manager.server.broadcast(PositionUpdated(self.network_id, self.pos.pos))

  def on_destroy_server(self):
    self.server_manager.server.broadcast(EntityDespawned(self.network_id))
