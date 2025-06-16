from dataclasses import dataclass

from .tile import Tile
from .empty import Empty

@dataclass
class PackedTileset:
  width: int
  height: int
  tiles: list

class Tileset:
  def unpack(ts):
    tiles = [Tile.unpack(t) for t in ts.tiles]
    return Tileset(ts.width, ts.height, tiles)

  def __init__(self, width, height, tiles=None):
    super().__init__()
    self.width = width
    self.height = height
    self.tiles = [Empty() for _ in range(width * height)] if tiles is None else tiles

  def pack(self):
    tiles = [t and t.pack() for t in self.tiles]
    return PackedTileset(self.width, self.height, tiles)

  def set_tile(self, x, y, tile):
    i = y * self.width + x
    self.tiles[i] = tile

  def get_tile(self, x, y):
    i = y * self.width + x
    return self.tiles[i]

  def itertiles(self):
    return ((x, y, self.get_tile(x, y)) for x in range(self.width) for y in range(self.height) if self.get_tile(x, y) is not None)
