from game.ecs import Component
from game.networking.events import PositionUpdated

#TODO: maybe merge into player once playercontroller is moved into client code
#TODO: replaced by actornetworking.. remove?
#TODO: make player networkable component? or make position networkable since that seems to be all this component does
#TODO: extend networking and rename to playernetworking
class ServerPlayer(Component):
  def __init__(self, server):
    super().__init__()
    #TODO: circular import
    from . import Id
    from ..actor import Player
    self.require(Player)
    self.require(Id)
    self.server = server
    self.id = None
    self.pos = None

  def start(self):
    #TODO: circular imports
    from ..physics import Position
    from . import Id
    self.id = self.get_component(Id).id
    self.pos = self.get_component(Position)

  def update(self):
    #TODO: spammy
    self.server.send(self.id, PositionUpdated(self.id, self.pos.pos))
