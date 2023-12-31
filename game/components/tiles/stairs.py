from game.utils.floor_transition import floor_transition
from ..core import Interactable
from . import TileEntity
import game.components as C

class Stairs(TileEntity, Interactable):
  def __init__(self, generator):
    super().__init__()
    self.require(C.Sprite, C.StairsNetworking, C.Networking)
    self.generator = generator

  def start(self):
    self.get_component(C.Sprite).set_sprite("assets/tiles/stairs.png")

  def interact(self, entity):
    #transition the game to the new world generated by our generator
    self.entity.world.find_component(C.GameMaster).game.transition(lambda world: floor_transition(world, self.generator))
