from .tile import Tile, TileType

class Wall(Tile):
  def __init__(self, y=1, height=1, type=TileType.WALL):
    super().__init__(type, solid=True, y=y, height=height)