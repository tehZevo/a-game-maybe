from .tile import Tile

class Floor(Tile):
  def __init__(self):
    self.image_path = "assets/tiles/floor.png"
    self.solid = False
