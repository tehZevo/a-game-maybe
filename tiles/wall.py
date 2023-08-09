from .tile import Tile

class Wall(Tile):
  def __init__(self):
    self.image_path = "assets/tiles/wall.png"
    self.solid = True
