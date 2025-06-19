from enum import IntEnum

TileType = IntEnum("TileType", [
  "EMPTY",
  "FLOOR", "FLOOR_ACCENT",
  "WALL", "WALL_ACCENT"
], start=0)

T = TileType

def is_floor(t):
  match t:
    case T.FLOOR | T.FLOOR_ACCENT: return True
  return False

def is_wall(t):
  match t:
    case T.WALL | T.WALL_ACCENT: return True
  return False

#TODO: pack all values in an integer
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
