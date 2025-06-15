from .tile import Tile, TileType

class Wall(Tile):
  def __init__(self, y=1, height=1):
    super().__init__(TileType.WALL, solid=True, y=y, height=height)