from game.ecs import Component
from game.networking.events import ActorSpawned, PositionUpdated
from ..networking import ServerManager
from ..physics import Position
from . import Id

#TODO: may need to make this more general (eg for tile entities)
#determine if we are on the client or the server
class ActorNetworking(Component):
  def __init__(self):
    super().__init__()
    #TODO: circular import
    from ..actor import Actor
    self.require(Actor)
    self.require(Id)
    self.server = None
    self.pos = None
    self.id = None

  #TODO: generalize this "is server" logic to a "NetworkedComponent"?
  def start(self):
    server_manager = self.entity.world.find_component(ServerManager)
    self.server = None if server_manager is None else server_manager.server

    if self.server is None:
      return

    self.pos = self.get_component(Position)
    self.id = self.get_component(Id)
    #TODO: send SpriteChanged?
    #spawn actor on clients
    self.server.broadcast(ActorSpawned(self.id.id))

  def update(self):
    if self.server is None:
      return

    #TODO: move to some kind of position/physics sync
    self.server.broadcast(PositionUpdated(self.id.id, self.pos.pos))

  def on_remove(self):
    #TODO: ActorRemoved
    pass
