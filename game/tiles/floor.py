from .tile import Tile, TileType

class Floor(Tile):
  def __init__(self):
    super().__init__(TileType.FLOOR, solid=False)
