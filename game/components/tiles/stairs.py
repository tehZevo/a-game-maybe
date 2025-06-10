from ..core import Interactable
from . import TileEntity
import game.components as C

class Stairs(TileEntity, Interactable):
  def __init__(self, mapdef):
    super().__init__()
    self.require(C.Sprite, C.SpriteSyncing, C.PositionSyncing, C.Networking)
    self.mapdef = mapdef

  def start(self):
    self.get_component(C.Sprite).set_sprite("assets/tiles/stairs.png")

  def interact(self, entity):
    self.entity.world.find_component(C.GameMaster).game.transition(self.mapdef)
