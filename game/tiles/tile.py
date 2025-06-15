from enum import IntEnum

#TODO: pack all values in an integer

TileType = IntEnum("TileType", ["EMPTY", "FLOOR", "WALL"])

class Tile:
  def unpack(t):
    return Tile(*t)
    
  def __init__(self, tile_type=TileType.EMPTY, solid=True, y=0, height=1):
    self.tile_type = tile_type
    self.solid = solid
    self.y = y
    self.height = height

  def pack(self):
    return [self.tile_type, self.solid, self.y, self.height]
