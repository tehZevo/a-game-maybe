from .tile import Tile, TileType

class Floor(Tile):
  def __init__(self, type=TileType.FLOOR):
    super().__init__(type, solid=False)
