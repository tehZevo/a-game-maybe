from components.tiles import TileEntity
from components import Sprite

class Floor(TileEntity):
  def __init__(self):
    super().__init__()
    self.require(Sprite)

  def start(self):
    self.get_component(Sprite).set_sprite("assets/tiles/floor.png")
