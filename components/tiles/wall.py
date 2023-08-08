from components.tiles import TileEntity
from components.graphics.sprite import Sprite

class Wall(TileEntity):
  def __init__(self):
    super().__init__()
    self.require(Sprite)
    self.solid = True

  def start(self):
    self.get_component(Sprite).set_sprite("assets/tiles/wall.png")
