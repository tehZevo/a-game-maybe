from dataclasses import dataclass

@dataclass
class Tile:
  image_path: str
  solid: bool

  def __init__(self, image_path=None, solid=None):
    self.image_path = image_path
    self.solid = solid
