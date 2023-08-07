from components.tiles import TileEntity
from components import Sprite

class Stairs(TileEntity):
  def __init__(self, generator):
    super().__init__()
    self.require(Sprite)
    self.generator = generator

  def start(self):
    self.get_component(Sprite).set_sprite("assets/tiles/stairs.png")
