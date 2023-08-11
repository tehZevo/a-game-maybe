from game.ecs import Component
from game.networking.events import PositionUpdated
from game.components.actor import Player
from game.components.networking import Id
from ..physics import Position

#TODO: maybe merge into player once playercontroller is moved into client code
#TODO: replaced by actornetworking.. remove?
class ServerPlayer(Component):
  def __init__(self, server):
    super().__init__()
    self.require(Player)
    self.require(Id)
    self.server = server
    self.id = None
    self.pos = None

  def start(self):
    self.id = self.get_component(Id).id
    self.pos = self.get_component(Position)

  def update(self):
    #TODO: spammy
    self.server.send(self.id, PositionUpdated(self.id, self.pos.pos))
