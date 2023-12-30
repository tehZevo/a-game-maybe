from game.ecs import Component
from game.networking.events import PositionUpdated
import game.components as C

#TODO: maybe merge into player once playercontroller is moved into client code
#TODO: replaced by actornetworking.. remove?
#TODO: make player networkable component? or make position networkable since that seems to be all this component does
#TODO: extend networking and rename to playernetworking

class ServerPlayer(Component):
  def __init__(self, server):
    super().__init__()
    self.require(C.Player, C.Networked, C.PositionSyncing)
    # self.server = server
    # self.id = None
    # self.pos = None

  # def start(self):
  #   self.id = self.get_component(C.Networked).id
  #   self.pos = self.get_component(C.Position)

  # def update(self):
  #   #TODO: spammy
  #   self.server.send(self.id, PositionUpdated(self.id, self.pos.pos))
